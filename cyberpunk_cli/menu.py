#!/usr/bin/env python3
"""
Cyberpunk Menu System - Core menu implementation

Professional terminal menu with retro aesthetics, mouse support,
and multiple input methods (keyboard, mouse, numbers).
"""

import os
import sys
import time
import signal
from pathlib import Path
from typing import List, Dict, Optional, Tuple, NamedTuple
from dataclasses import dataclass

try:
    import termios
    import tty
    TERMIOS_AVAILABLE = True
except ImportError:
    TERMIOS_AVAILABLE = False

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align

from .themes import theme_manager


class MenuOption(NamedTuple):
    """Menu option data structure"""
    key: str
    name: str
    description: str


class CyberpunkMenu:
    """Cyberpunk-themed terminal menu with retro aesthetics"""
    
    def __init__(self, title: str = "Cyberpunk Menu", theme: str = "fallout"):
        self.title = title
        self.options: List[MenuOption] = []
        self.selected_index = 0
        self.console = Console()
        
        # Mouse support
        self.menu_start_line = 0
        self.last_click_time = 0
        self.last_click_index = -1
        
        # Set theme
        if not theme_manager.set_theme(theme):
            theme_manager.set_theme("fallout")  # Fallback
    
    def add_option(self, key: str, name: str, description: str) -> "CyberpunkMenu":
        """Add a menu option (fluent interface)"""
        self.options.append(MenuOption(key, name, description))
        return self
    
    def add_separator(self) -> "CyberpunkMenu":
        """Add a visual separator"""
        self.options.append(MenuOption("separator", "───", ""))
        return self
    
    def add_exit(self, name: str = "❌ Exit", description: str = "Quit the application") -> "CyberpunkMenu":
        """Add exit option"""
        self.options.append(MenuOption("exit", name, description))
        return self
    
    def get_key(self):
        """Get a single keypress from stdin with mouse support"""
        if sys.platform == 'win32':
            try:
                import msvcrt
                return msvcrt.getch().decode('utf-8')
            except ImportError:
                return input().strip() or '\n'
        else:
            if not TERMIOS_AVAILABLE:
                return input().strip() or '\n'
            
            try:
                fd = sys.stdin.fileno()
                if not os.isatty(fd):
                    return input().strip() or '\n'
                
                # Enable mouse reporting
                sys.stdout.write('\x1b[?1000h')  # Enable mouse tracking
                sys.stdout.flush()
                    
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setcbreak(fd)
                    key = sys.stdin.read(1)
                    if key == '\x1b':  # ESC sequence
                        # Try to read full escape sequence
                        try:
                            next_char = sys.stdin.read(1)
                            if next_char == '[':
                                # Could be arrow key or mouse
                                third_char = sys.stdin.read(1)
                                if third_char == 'M':
                                    # Mouse event - read 3 more bytes
                                    mouse_data = sys.stdin.read(3)
                                    return '\x1b[M' + mouse_data
                                else:
                                    key += next_char + third_char
                            else:
                                key += next_char
                        except:
                            pass
                    return key
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    # Disable mouse reporting
                    sys.stdout.write('\x1b[?1000l')
                    sys.stdout.flush()
            except (termios.error, OSError, AttributeError):
                # Fallback to regular input for non-TTY environments
                return input().strip() or '\n'
    
    def handle_mouse_event(self, mouse_data: str) -> Optional[str]:
        """Handle mouse click events"""
        if len(mouse_data) < 6 or not mouse_data.startswith('\x1b[M'):
            return None
            
        # Parse mouse event
        button = ord(mouse_data[3]) - 32
        col = ord(mouse_data[4]) - 32
        row = ord(mouse_data[5]) - 32
        
        # Check if click is on a menu item
        menu_row = row - self.menu_start_line
        if 0 <= menu_row < len(self.options):
            # Skip separators
            if self.options[menu_row].key == "separator":
                return None
                
            # Calculate double-click
            current_time = time.time()
            is_double_click = (
                current_time - self.last_click_time < 0.5 and
                menu_row == self.last_click_index
            )
            
            self.last_click_time = current_time
            self.last_click_index = menu_row
            
            # Update selection
            self.selected_index = menu_row
            
            if is_double_click:
                return '\n'  # Double-click executes
            else:
                return 'click'  # Single click just selects
        
        return None
    
    def render_menu(self) -> None:
        """Render the menu using current theme"""
        theme = theme_manager.get_theme()
        if not theme:
            self.console.print("[red]Error: No theme available[/red]")
            return
            
        self.console.clear()
        
        # Get terminal width for responsive layout
        terminal_width = self.console.size.width
        
        # Render theme-specific elements
        theme.render_logo(self.console)
        theme.render_subtitle(self.console)
        
        # Track menu start position for mouse clicks
        if terminal_width >= 80:
            self.menu_start_line = 18  # Full logo + subtitle + spacing
        else:
            self.menu_start_line = 8   # Compact logo + subtitle + spacing
        
        # Render menu items
        for i, option in enumerate(self.options):
            if option.key == "separator":
                separator = theme.render_separator(option.name)
                self.console.print(separator)
            else:
                is_selected = (i == self.selected_index)
                menu_line = theme.render_menu_item(option.name, option.description, is_selected)
                self.console.print(menu_line)
        
        # Render footer
        theme.render_footer(self.console)
    
    def run(self) -> Optional[str]:
        """Run the interactive menu and return selected option key"""
        theme = theme_manager.get_theme()
        if not theme:
            self.console.print("[red]Error: No theme available[/red]")
            return None
            
        self.console.print(theme.get_loading_message())
        time.sleep(0.5)  # Brief loading effect
        
        while True:
            self.render_menu()
            
            try:
                key = self.get_key()
                
                # Handle mouse events
                if isinstance(key, str) and key.startswith('\x1b[M'):
                    mouse_result = self.handle_mouse_event(key)
                    if mouse_result == '\n':  # Double-click
                        option = self.options[self.selected_index]
                        if option.key == "exit":
                            self.console.print(theme.get_goodbye_message())
                            return None
                        else:
                            self.console.clear()
                            self.console.print(theme.get_execution_message(option.name))
                            time.sleep(0.3)
                            return option.key
                    elif mouse_result == 'click':
                        # Single click just updates selection, re-render
                        continue
                
                # Arrow key navigation
                elif key == '\x1b[A':  # Up arrow
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                    # Skip separators
                    while self.options[self.selected_index].key == "separator":
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                        
                elif key == '\x1b[B':  # Down arrow
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                    # Skip separators
                    while self.options[self.selected_index].key == "separator":
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                        
                elif key in ['\r', '\n']:  # Enter
                    option = self.options[self.selected_index]
                    if option.key == "exit":
                        self.console.print(theme.get_goodbye_message())
                        return None
                    elif option.key == "separator":
                        continue  # Can't select separators
                    else:
                        self.console.clear()
                        self.console.print(theme.get_execution_message(option.name))
                        time.sleep(0.3)
                        return option.key
                        
                elif key in ['\x1b', 'q', 'Q']:  # ESC or Q
                    self.console.print(theme.get_goodbye_message())
                    return None
                    
                elif key.isdigit():  # Number key shortcuts
                    num = int(key)
                    if 0 <= num < len(self.options):
                        option = self.options[num]
                        if option.key == "separator":
                            continue
                        self.selected_index = num
                        if option.key == "exit":
                            self.console.print(theme.get_goodbye_message())
                            return None
                        else:
                            self.console.clear()
                            self.console.print(theme.get_execution_message(option.name))
                            time.sleep(0.3)
                            return option.key
                        
            except (KeyboardInterrupt, EOFError):
                self.console.print(theme.get_goodbye_message())
                return None