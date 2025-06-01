#!/usr/bin/env python3
"""
Cyberpunk Terminal Menu Themes
Professional terminal interface theming system with auto-discovery
"""

import os
import importlib
from pathlib import Path
from .base_theme import BaseTheme, ThemeManager, theme_manager

# Auto-discover and register all theme classes
def _discover_themes():
    """Auto-discover theme classes from *_theme.py files"""
    themes_dir = Path(__file__).parent
    
    for theme_file in themes_dir.glob("*_theme.py"):
        if theme_file.name == "base_theme.py":
            continue
            
        module_name = theme_file.stem
        try:
            module = importlib.import_module(f".{module_name}", package=__name__)
            
            # Find theme class (should end with "Theme")
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (isinstance(attr, type) and 
                    issubclass(attr, BaseTheme) and 
                    attr != BaseTheme):
                    theme_manager.register_theme(attr())
                    break
        except ImportError:
            continue

# Auto-discover themes
_discover_themes()

# Set default theme
theme_manager.set_theme("loki")

__all__ = [
    "BaseTheme",
    "ThemeManager", 
    "theme_manager"
]

__version__ = "1.0.0"