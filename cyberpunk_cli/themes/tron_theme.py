#!/usr/bin/env python3
"""
Tron Theme - Blue neon cyberpunk aesthetic
Inspired by the Tron digital world interface
"""

from .base_theme import BaseTheme
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from typing import Dict


class TronTheme(BaseTheme):
    """Tron-inspired blue neon theme"""
    
    def __init__(self):
        super().__init__()
        self.name = "tron"
        self.description = "Neon cyberpunk interface from Tron"
        
    def get_colors(self) -> Dict[str, str]:
        return {
            "primary": "bright_cyan",        # Tron blue
            "secondary": "cyan",             # Darker blue
            "accent": "bright_white",        # White highlights
            "background": "black",           # Terminal background
            "warning": "bright_red",         # Warning/error text
            "success": "bright_blue",        # Success indicators
            "border": "cyan",                # Panel borders
            "selected": "black on bright_cyan",  # Selection highlight
            "dim": "color(24)",              # Dim blue
            "neon": "bright_magenta",        # Neon accents
        }
    
    def render_logo(self, console) -> None:
        """Render Tron-style neon logo"""
        colors = self.get_colors()
        
        logo = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║  ░██████╗░███╗░░░███╗░█████╗░██████╗░████████╗      ░█████╗░██╗           ║
║  ██╔════╝░████╗░████║██╔══██╗██╔══██╗╚══██╔══╝     ██╔══██╗██║           ║
║  ╚█████╗░░██╔████╔██║███████║██████╔╝░░░██║░░░████████║░░██║██║           ║
║  ░╚═══██╗░██║╚██╔╝██║██╔══██║██╔══██╗░░░██║░░░╚═════██║░░██║██║           ║
║  ██████╔╝░██║░╚═╝░██║██║░░██║██║░░██║░░░██║░░░░░░░░░╚█████╔╝██║           ║
║  ╚═════╝░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░░░░╚════╝░╚═╝           ║
║                                                                           ║
║  ████████████████████████████████████████████████████████████████████████ ║
║  █░░░░░░░     DIGITAL FRONTIER GRID SYSTEM v7.0      ░░░░░░░█            ║
║  █        ⬢⬢⬢ WELCOME TO THE GRID, PROGRAM ⬢⬢⬢        █            ║
║  ████████████████████████████████████████████████████████████████████████ ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝"""
        
        # Create neon gradient effect
        lines = logo.split('\n')
        for i, line in enumerate(lines):
            if i < 3:
                style = colors["dim"]
            elif i < 6:
                style = colors["secondary"] 
            elif i < 9:
                style = colors["primary"]
            elif i == 10:
                style = colors["neon"]
            else:
                style = colors["success"]
            console.print(Text(line, style=style))
    
    def render_subtitle(self, console) -> None:
        """Render Tron subtitle panel"""
        colors = self.get_colors()
        
        subtitle_text = Text()
        subtitle_text.append("⬢ ", style=colors["neon"])
        subtitle_text.append("GRID VALIDATION PROTOCOL", style=f"bold {colors['primary']}")
        subtitle_text.append(" ⬢ ", style=colors["neon"])
        subtitle_text.append("NEON PROCESSING CORE", style=colors["secondary"])
        subtitle_text.append(" ⬢ ", style=colors["neon"])
        subtitle_text.append("Build.7.0", style=f"bold {colors['primary']}")
        subtitle_text.append(" ⬢", style=colors["neon"])
        
        subtitle = Panel.fit(
            Align.center(subtitle_text),
            border_style=colors["border"],
            padding=(0, 1),
            title=f"[{colors['neon']}]▲ DIGITAL FRONTIER INTERFACE ▲[/{colors['neon']}]",
            title_align="center"
        )
        console.print(subtitle)
        console.print()
    
    def render_menu_item(self, name: str, desc: str, selected: bool) -> Text:
        """Render Tron-style menu item"""
        colors = self.get_colors()
        
        if selected:
            style = colors["selected"]
            prefix = "▶ "
            suffix = " ◀"
            accent_style = colors["neon"]
        else:
            style = colors["primary"]
            prefix = "  "
            suffix = "  "
            accent_style = colors["dim"]
        
        menu_line = Text()
        menu_line.append("  ▲ ", style=accent_style)
        menu_line.append(f"{prefix}{name:<25}", style=style)
        menu_line.append(f"{desc}{suffix}", style=style if selected else colors["dim"])
        
        return menu_line
    
    def render_separator(self, title: str = "") -> Text:
        """Render Tron section separator"""
        colors = self.get_colors()
        if title:
            separator = Text("  ▲ ", style=colors["success"]) + \
                       Text("▬" * 30 + f" ⬢ {title} ⬢ " + "▬" * 30, style=colors["success"])
        else:
            separator = Text("  ▲ ", style=colors["success"]) + \
                       Text("▬" * 70, style=colors["success"])
        return separator
    
    def render_footer(self, console) -> None:
        """Render Tron control panel"""
        colors = self.get_colors()
        
        controls = Text()
        controls.append("⬢ ", style=colors["neon"])
        controls.append("GRID INTERFACE", style=f"bold {colors['primary']}")
        controls.append(" ⬢  ", style=colors["neon"])
        controls.append("↑↓", style=colors["success"])
        controls.append(" Navigate  ", style=colors["secondary"])
        controls.append("⟨ENTER⟩", style=colors["success"])
        controls.append(" Execute  ", style=colors["secondary"])
        controls.append("⟨ESC⟩", style=colors["warning"])
        controls.append(" Derezzz  ", style=colors["secondary"])
        controls.append("⟨DISC⟩", style=colors["neon"])
        controls.append(" Identity Disc", style=colors["secondary"])
        
        footer = Panel.fit(
            Align.center(controls),
            border_style=colors["border"],
            title=f"[{colors['neon']}]▲ PROGRAM EXECUTION GRID ▲[/{colors['neon']}]",
            title_align="center",
            padding=(0, 1)
        )
        console.print()
        console.print(footer)
    
    def get_loading_message(self) -> str:
        return "[dim]⬢ Entering the Grid... ⬢[/dim]"
    
    def get_execution_message(self, action: str) -> str:
        colors = self.get_colors()
        return f"[{colors['success']}]⬢ REZZING:[/{colors['success']}] [{colors['primary']}]{action}[/{colors['primary']}]"
    
    def get_goodbye_message(self) -> str:
        colors = self.get_colors()
        return f"\n[{colors['primary']}]⬢ End of line, program... ⬢[/{colors['primary']}]"