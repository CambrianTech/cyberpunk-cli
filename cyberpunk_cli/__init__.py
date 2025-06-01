#!/usr/bin/env python3
"""
Cyberpunk CLI - Professional terminal interface framework

Transform any CLI into a retro-futuristic cyberpunk terminal with zero effort.
Works standalone or integrates seamlessly with Click applications.

Zero-effort enhancement:
    import cyberpunk_cli  # Just add this line to any Click app!
    
Full decorator framework:
    from cyberpunk_cli import cyberpunk
    
    @cyberpunk(title="My App", theme="loki")
    def main():
        '''My awesome CLI application'''
        print("Hello cyberpunk world!")
"""

# Core components
from .menu import CyberpunkMenu, MenuOption
from .themes import theme_manager, BaseTheme
from .themes.fallout_theme import FalloutTheme
from .themes.matrix_theme import MatrixTheme  
from .themes.tron_theme import TronTheme

# Main decorator system
from .decorator import cyberpunk, option, group, enhance_click_app

# Auto-enhancement for Click (when just importing cyberpunk_cli)
import sys

try:
    import click as _click
    
    # Store original Click decorators
    _original_command = _click.command
    _original_group = _click.group
    
    def _auto_enhance_command(*args, **kwargs):
        """Auto-enhanced Click command decorator"""
        def decorator(func):
            click_func = _original_command(*args, **kwargs)(func)
            
            # Auto-enhance with cyberpunk interface when no CLI args
            if len(sys.argv) <= 1:
                return cyberpunk(click_integration="integrate")(click_func)
            else:
                return click_func
        return decorator
    
    def _auto_enhance_group(*args, **kwargs):
        """Auto-enhanced Click group decorator"""
        def decorator(func):
            click_func = _original_group(*args, **kwargs)(func)
            
            # Auto-enhance with cyberpunk interface when no CLI args
            if len(sys.argv) <= 1:
                return cyberpunk(click_integration="integrate")(click_func)
            else:
                return click_func
        return decorator
    
    # Enable zero-effort enhancement by replacing Click decorators
    _click.command = _auto_enhance_command
    _click.group = _auto_enhance_group
    
except ImportError:
    # Click not available, skip auto-enhancement
    pass

__version__ = "1.0.0"
__author__ = "Cambrian"
__email__ = "contact@cambrian.io"

__all__ = [
    # Core classes
    "CyberpunkMenu",
    "MenuOption", 
    "theme_manager",
    "BaseTheme",
    "FalloutTheme",
    "MatrixTheme",
    "TronTheme",
    
    # Decorator system
    "cyberpunk", 
    "option",
    "group",
    "enhance_click_app"
]