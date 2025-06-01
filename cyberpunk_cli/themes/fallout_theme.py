#!/usr/bin/env python3
"""
Fallout Theme - Retro-futuristic terminal interface
Inspired by the Vault-Tec terminals from the Fallout universe
"""

from .base_theme import BaseTheme
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from typing import Dict


class FalloutTheme(BaseTheme):
    """Fallout-inspired retro terminal theme"""
    
    def __init__(self):
        super().__init__()
        self.name = "fallout"
        self.description = "Vault-Tec terminal interface"
        
    def get_colors(self) -> Dict[str, str]:
        return {
            "primary": "bright_yellow",      # Amber terminal text
            "secondary": "yellow",           # Darker amber
            "accent": "bright_white",        # White highlights
            "background": "black",           # Terminal background
            "warning": "bright_red",         # Warning/error text
            "success": "bright_green",       # Success indicators
            "border": "yellow",              # Panel borders
            "selected": "black on bright_yellow",  # Selection highlight
            "dim": "color(94)",              # Dim text (dark amber)
        }
    
    def render_logo(self, console) -> None:
        """Render Vault-Tec style logo"""
        colors = self.get_colors()
        
        logo = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║    █████████╗███╗   ███╗ █████╗ ██████╗ ████████╗      ██████╗██╗         ║
║    ██╔══════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝     ██╔════╝██║         ║
║    ███████╗ ██╔████╔██║███████║██████╔╝   ██║  █████╗██║     ██║         ║
║    ╚════██║ ██║╚██╔╝██║██╔══██║██╔══██╗   ██║  ╚════╝██║     ██║         ║
║    ███████║ ██║ ╚═╝ ██║██║  ██║██║  ██║   ██║        ╚██████╗██║         ║
║    ╚══════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝         ╚═════╝╚═╝         ║
║                                                                           ║
║  ████████████████████████████████████████████████████████████████████████ ║
║  █                    VAULT-TEC TERMINAL v2.077                        █ ║
║  █                      [ ACCESS AUTHORIZED ]                          █ ║
║  ████████████████████████████████████████████████████████████████████████ ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝"""
        
        console.print(Text(logo, style=colors["primary"]))
    
    def render_subtitle(self, console) -> None:
        """Render Vault-Tec subtitle panel"""
        colors = self.get_colors()
        
        subtitle_text = Text()
        subtitle_text.append("*** ", style=colors["accent"])
        subtitle_text.append("VAULT-TEC AUTOMATED SYSTEMS", style=f"bold {colors['primary']}")
        subtitle_text.append(" *** ", style=colors["accent"])
        subtitle_text.append("CONTINUOUS INTEGRATION PROTOCOL", style=colors["secondary"])
        subtitle_text.append(" *** ", style=colors["accent"])
        subtitle_text.append("Build 2.077", style=f"bold {colors['primary']}")
        subtitle_text.append(" ***", style=colors["accent"])
        
        subtitle = Panel.fit(
            Align.center(subtitle_text),
            border_style=colors["border"],
            padding=(0, 1),
            title=f"[{colors['accent']}]█ ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM █[/{colors['accent']}]",
            title_align="center"
        )
        console.print(subtitle)
        console.print()
    
    def render_menu_item(self, name: str, desc: str, selected: bool) -> Text:
        """Render Fallout-style menu item"""
        colors = self.get_colors()
        
        if selected:
            style = colors["selected"]
            prefix = "> "
            suffix = " <"
            accent_style = colors["primary"]
        else:
            style = colors["primary"]
            prefix = "  "
            suffix = "  "
            accent_style = colors["dim"]
        
        menu_line = Text()
        menu_line.append("  █ ", style=accent_style)
        menu_line.append(f"{prefix}{name:<25}", style=style)
        menu_line.append(f"{desc}{suffix}", style=style if selected else colors["dim"])
        
        return menu_line
    
    def render_separator(self, title: str = "") -> Text:
        """Render Vault-Tec section separator"""
        colors = self.get_colors()
        if title:
            separator = Text("  █ ", style=colors["success"]) + \
                       Text("═" * 50 + f" *** {title} *** " + "═" * 15, style=colors["success"])
        else:
            separator = Text("  █ ", style=colors["success"]) + \
                       Text("═" * 70, style=colors["success"])
        return separator
    
    def render_footer(self, console) -> None:
        """Render Vault-Tec control panel"""
        colors = self.get_colors()
        
        controls = Text()
        controls.append("*** ", style=colors["accent"])
        controls.append("TERMINAL CONTROLS", style=f"bold {colors['primary']}")
        controls.append(" ***  ", style=colors["accent"])
        controls.append("↑↓", style=colors["success"])
        controls.append(" Navigate  ", style=colors["secondary"])
        controls.append("[ENTER]", style=colors["success"])
        controls.append(" Execute  ", style=colors["secondary"])
        controls.append("[ESC]", style=colors["warning"])
        controls.append(" Disconnect  ", style=colors["secondary"])
        controls.append("[MOUSE]", style=colors["accent"])
        controls.append(" Point Interface", style=colors["secondary"])
        
        footer = Panel.fit(
            Align.center(controls),
            border_style=colors["border"],
            title=f"[{colors['accent']}]█ VAULT-TEC INTERFACE PROTOCOL █[/{colors['accent']}]",
            title_align="center",
            padding=(0, 1)
        )
        console.print()
        console.print(footer)
    
    def get_loading_message(self) -> str:
        return "[dim]*** INITIALIZING VAULT-TEC TERMINAL ***[/dim]"
    
    def get_execution_message(self, action: str) -> str:
        colors = self.get_colors()
        return f"[{colors['success']}]*** EXECUTING:[/{colors['success']}] [{colors['primary']}]{action}[/{colors['primary']}]"
    
    def get_goodbye_message(self) -> str:
        colors = self.get_colors()
        return f"\n[{colors['primary']}]*** HAVE A PLEASANT DAY, VAULT DWELLER ***[/{colors['primary']}]"