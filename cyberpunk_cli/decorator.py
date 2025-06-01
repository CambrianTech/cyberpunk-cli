#!/usr/bin/env python3
"""
Cyberpunk CLI Decorator System
Unified decorator that works with or without Click, with easy title customization
"""

import json
import sys
import os
import inspect
from pathlib import Path
from typing import Optional, Callable, Dict, Any, List
from functools import wraps
import click
from .menu import CyberpunkMenu
from .themes import theme_manager


def load_theme_config() -> Dict[str, Any]:
    """Load shared theme configuration"""
    config_path = Path(__file__).parent / "themes" / "theme_config.json"
    with open(config_path, 'r') as f:
        return json.load(f)


class CyberpunkDecorator:
    """Main cyberpunk decorator that integrates with Click or works standalone"""
    
    def __init__(self, 
                 title: Optional[str] = None,
                 theme: str = "loki", 
                 theme_switching: bool = True,
                 click_integration: str = "override"):
        """
        Args:
            title: Custom terminal title (auto-detected from function if None)
            theme: Default theme name
            theme_switching: Allow Ctrl+T theme switching
            click_integration: "override" (default), "integrate", or "disable"
        """
        self.title = title
        self.theme = theme
        self.theme_switching = theme_switching
        self.click_integration = click_integration
        self.theme_config = load_theme_config()
        
    def __call__(self, func: Callable) -> Callable:
        """Main decorator function"""
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Auto-detect title if not provided
            if self.title is None:
                # Try to get from docstring
                if func.__doc__:
                    title = func.__doc__.strip().split('\n')[0]
                else:
                    # Generate from function name
                    title = func.__name__.replace('_', ' ').title()
            else:
                title = self.title
                
            # Check if we have CLI args (if so, run normally)
            if len(sys.argv) > 1 and self.click_integration != "disable":
                # We have CLI arguments, run the function normally
                if self._is_click_command(func):
                    return func(*args, **kwargs)
                else:
                    # Parse basic arguments for non-Click functions
                    return self._handle_basic_args(func, *args, **kwargs)
            
            # No CLI args, show cyberpunk menu
            return self._show_cyberpunk_interface(func, title, *args, **kwargs)
            
        # Handle Click integration
        if self._is_click_command(func):
            return self._integrate_with_click(wrapper, func)
        else:
            return wrapper
    
    def _is_click_command(self, func: Callable) -> bool:
        """Check if function is a Click command"""
        return hasattr(func, '__click_params__') or hasattr(func, 'callback')
    
    def _integrate_with_click(self, wrapper: Callable, original_func: Callable) -> Callable:
        """Integrate with existing Click command"""
        if self.click_integration == "override":
            # Replace Click behavior entirely
            return wrapper
        elif self.click_integration == "integrate":
            # Keep Click but add cyberpunk menu when no args
            original_func._cyberpunk_wrapper = wrapper
            return original_func
        else:
            return original_func
    
    def _extract_click_options(self, func: Callable) -> List[Dict[str, Any]]:
        """Extract Click options to create menu items"""
        options = []
        if hasattr(func, '__click_params__'):
            for param in func.__click_params__:
                if isinstance(param, click.Option):
                    options.append({
                        'name': param.name,
                        'help': param.help or f"Set {param.name}",
                        'is_flag': param.is_flag,
                        'default': param.default
                    })
        return options
    
    def _show_cyberpunk_interface(self, func: Callable, title: str, *args, **kwargs) -> Any:
        """Show the cyberpunk terminal interface"""
        theme_manager.set_theme(self.theme)
        menu = CyberpunkMenu(title, theme=self.theme)
        
        # If it's a Click command, extract options as menu items
        if self._is_click_command(func):
            click_options = self._extract_click_options(func)
            for option in click_options:
                menu.add_option(
                    option['name'],
                    option['name'].replace('_', ' ').title(),
                    option['help']
                )
        else:
            # For non-Click functions, create basic menu
            sig = inspect.signature(func)
            for param_name, param in sig.parameters.items():
                if param.annotation != inspect.Parameter.empty:
                    help_text = f"Set {param_name} ({param.annotation.__name__})"
                else:
                    help_text = f"Set {param_name}"
                    
                menu.add_option(param_name, param_name.replace('_', ' ').title(), help_text)
        
        # Add theme switching if enabled
        if self.theme_switching:
            menu.add_separator("Settings")
            menu.add_option("change_theme", "Change Theme", "Switch cyberpunk theme")
        
        menu.add_exit()
        
        # Run the menu
        while True:
            choice = menu.run()
            
            if choice is None:  # Exit
                break
            elif choice == "change_theme":
                self._show_theme_selector()
                menu = CyberpunkMenu(title, theme=theme_manager.get_theme().name)  # Recreate with new theme
            else:
                # Handle the selected option
                return self._handle_menu_choice(func, choice, *args, **kwargs)
    
    def _show_theme_selector(self):
        """Show theme selection interface"""
        themes = self.theme_config['themes']
        theme_menu = CyberpunkMenu("Theme Selector")
        
        for theme_name, theme_data in themes.items():
            theme_menu.add_option(
                theme_name,
                theme_data['display_name'],
                theme_data['description']
            )
        
        theme_menu.add_exit("Back to Main Menu")
        
        choice = theme_menu.run()
        if choice and choice in themes:
            theme_manager.set_theme(choice)
            print(f"Theme changed to {themes[choice]['display_name']}")
            input("Press Enter to continue...")
    
    def _handle_menu_choice(self, func: Callable, choice: str, *args, **kwargs) -> Any:
        """Handle menu selection and execute function"""
        if self._is_click_command(func):
            # For Click commands, we need to simulate CLI args
            sys.argv = [sys.argv[0], f'--{choice}']
            return func(*args, **kwargs)
        else:
            # For regular functions, prompt for parameter value
            sig = inspect.signature(func)
            if choice in sig.parameters:
                param = sig.parameters[choice]
                value = input(f"Enter value for {choice}: ")
                
                # Basic type conversion
                if param.annotation == int:
                    value = int(value)
                elif param.annotation == bool:
                    value = value.lower() in ('true', 'yes', '1', 'on')
                
                kwargs[choice] = value
                
            return func(*args, **kwargs)
    
    def _handle_basic_args(self, func: Callable, *args, **kwargs) -> Any:
        """Handle basic command line arguments for non-Click functions"""
        # Simple argument parsing for non-Click functions
        # This is a basic implementation - could be expanded
        return func(*args, **kwargs)


# Main decorator function
def cyberpunk(title: Optional[str] = None,
              theme: str = "loki", 
              theme_switching: bool = True,
              click_integration: str = "override") -> Callable:
    """
    Cyberpunk CLI decorator that works with or without Click
    
    Args:
        title: Custom terminal title (auto-detected if None)
        theme: Default theme ("loki", "matrix", "fallout", "tron")
        theme_switching: Enable Ctrl+T theme switching
        click_integration: "override" (replace Click), "integrate" (enhance Click), "disable"
    
    Examples:
        # Basic usage
        @cyberpunk
        def my_app():
            '''My Amazing App'''
            print("Hello World")
        
        # Custom title and theme
        @cyberpunk(title="DevOps Console", theme="fallout")
        def deploy():
            print("Deploying...")
        
        # Work with existing Click command
        @cyberpunk(click_integration="integrate")
        @click.command()
        @click.option('--env', help='Environment')
        def deploy(env):
            print(f"Deploying to {env}")
    """
    return CyberpunkDecorator(title, theme, theme_switching, click_integration)


# Convenience functions for common patterns
def option(name: str, help: str = "", **kwargs):
    """Cyberpunk option decorator (compatible with Click)"""
    def decorator(func):
        if not hasattr(func, '_cyberpunk_options'):
            func._cyberpunk_options = []
        func._cyberpunk_options.append({'name': name, 'help': help, **kwargs})
        return func
    return decorator


def group():
    """Cyberpunk group decorator"""
    def decorator(func):
        func._cyberpunk_group = True
        return func
    return decorator


# Auto-enhancement for existing Click apps
def enhance_click_app(click_func: Callable, **cyberpunk_options) -> Callable:
    """
    Enhance existing Click application with cyberpunk interface
    
    Args:
        click_func: Existing Click command/group
        **cyberpunk_options: Options to pass to @cyberpunk decorator
    
    Example:
        import click
        from cyberpunk_cli import enhance_click_app
        
        @click.command()
        def existing_cli():
            pass
            
        enhanced_cli = enhance_click_app(existing_cli, theme="matrix")
    """
    decorator = cyberpunk(**cyberpunk_options)
    return decorator(click_func)