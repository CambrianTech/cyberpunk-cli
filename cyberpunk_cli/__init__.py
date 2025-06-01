#!/usr/bin/env python3
"""
Cyberpunk CLI - Terminal menu system with retro themes

A professional terminal interface library with cyberpunk aesthetics,
featuring multiple retro themes inspired by Fallout, Matrix, and Tron.

Example usage:
    from cyberpunk_cli import CyberpunkMenu
    
    menu = CyberpunkMenu("My Application")
    menu.add_option("deploy", "🚀 Deploy", "Deploy to production")
    menu.add_option("test", "🧪 Test", "Run test suite") 
    
    choice = menu.run()
"""

from .menu import CyberpunkMenu, MenuOption
from .themes import theme_manager, BaseTheme
from .themes.fallout_theme import FalloutTheme
from .themes.matrix_theme import MatrixTheme  
from .themes.tron_theme import TronTheme

__version__ = "1.0.0"
__author__ = "CambrianTech"
__email__ = "contact@cambriantech.com"

__all__ = [
    "CyberpunkMenu",
    "MenuOption", 
    "theme_manager",
    "BaseTheme",
    "FalloutTheme",
    "MatrixTheme",
    "TronTheme",
]