#!/usr/bin/env python3
"""
Base Theme System for Cyberpunk CI Validator
Professional terminal interface theming system
"""

from abc import ABC, abstractmethod
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from typing import Dict, List, Tuple


class BaseTheme(ABC):
    """Abstract base class for terminal themes"""
    
    def __init__(self):
        self.name = "base"
        self.description = "Base theme class"
        
    @abstractmethod
    def get_colors(self) -> Dict[str, str]:
        """Return theme color palette"""
        pass
    
    @abstractmethod
    def render_logo(self, console) -> None:
        """Render the main logo/header"""
        pass
    
    @abstractmethod
    def render_subtitle(self, console) -> None:
        """Render the subtitle/description panel"""
        pass
    
    @abstractmethod
    def render_menu_item(self, name: str, desc: str, selected: bool) -> Text:
        """Render a single menu item"""
        pass
    
    @abstractmethod
    def render_separator(self, title: str = "") -> Text:
        """Render a section separator"""
        pass
    
    @abstractmethod
    def render_footer(self, console) -> None:
        """Render the footer/controls panel"""
        pass
    
    @abstractmethod
    def get_loading_message(self) -> str:
        """Return theme-appropriate loading message"""
        pass
    
    @abstractmethod
    def get_execution_message(self, action: str) -> str:
        """Return theme-appropriate execution message"""
        pass
    
    @abstractmethod
    def get_goodbye_message(self) -> str:
        """Return theme-appropriate goodbye message"""
        pass


class ThemeManager:
    """Manages theme loading and switching"""
    
    def __init__(self):
        self.themes = {}
        self.current_theme = None
        
    def register_theme(self, theme: BaseTheme):
        """Register a new theme"""
        self.themes[theme.name] = theme
        
    def set_theme(self, theme_name: str):
        """Set the active theme"""
        if theme_name in self.themes:
            self.current_theme = self.themes[theme_name]
            return True
        return False
        
    def get_theme(self) -> BaseTheme:
        """Get the current active theme"""
        return self.current_theme
        
    def list_themes(self) -> List[str]:
        """List available theme names"""
        return list(self.themes.keys())


# Global theme manager instance
theme_manager = ThemeManager()