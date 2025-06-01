#!/usr/bin/env python3
"""
Cyberpunk Terminal Menu Themes
Professional terminal interface theming system

Available Themes:
- loki: Norse mythology Asgardian interface
- fallout: Vault-Tec terminal interface
- matrix: Digital rain from The Matrix
- tron: Neon cyberpunk from Tron
"""

from .base_theme import BaseTheme, ThemeManager, theme_manager
from .loki_theme import LokiTheme
from .fallout_theme import FalloutTheme
from .matrix_theme import MatrixTheme
from .tron_theme import TronTheme

# Auto-register all themes
theme_manager.register_theme(LokiTheme())
theme_manager.register_theme(FalloutTheme())
theme_manager.register_theme(MatrixTheme())
theme_manager.register_theme(TronTheme())

# Set default theme
theme_manager.set_theme("loki")

__all__ = [
    "BaseTheme",
    "ThemeManager", 
    "theme_manager",
    "LokiTheme",
    "FalloutTheme",
    "MatrixTheme",
    "TronTheme"
]

__version__ = "1.0.0"