#!/usr/bin/env python3
"""
Matrix Theme - Green code rain aesthetic
Inspired by The Matrix digital world interface
"""

from .base_theme import BaseTheme
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from typing import Dict


class MatrixTheme(BaseTheme):
    """Matrix-inspired green code theme"""
    
    def __init__(self):
        super().__init__()
        self.name = "matrix"
        self.description = "Digital rain interface from The Matrix"
        
    def get_colors(self) -> Dict[str, str]:
        return {
            "primary": "bright_green",       # Matrix green
            "secondary": "green",            # Darker green
            "accent": "bright_white",        # White highlights
            "background": "black",           # Terminal background
            "warning": "bright_red",         # Warning/error text
            "success": "bright_green",       # Success indicators
            "border": "green",               # Panel borders
            "selected": "black on bright_green",  # Selection highlight
            "dim": "color(22)",              # Dim green
        }
    
    def render_logo(self, console) -> None:
        """Render Matrix-style digital logo"""
        colors = self.get_colors()
        
        logo = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▓▓██████╗███╗   ███╗ █████╗ ██████╗ ████████╗      ██████╗██╗▓▓▓▓▓▓▓▓▓▓
▓▓██╔═══╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝     ██╔════╝██║▓▓░░░░░░░░░
▓▓███████╗██╔████╔██║███████║██████╔╝   ██║ ░░░░░░██║     ██║▓▓▓▓▓▓▓▓▓▓
▓▓╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║ ░░░░░░██║     ██║▓▓░░░░░░░░░
▓▓███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║       ╚██████╗██║▓▓▓▓▓▓▓▓▓▓
▓▓╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝╚═╝▓▓░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
░░░░  WELCOME TO THE REAL WORLD - DIGITAL VALIDATION MATRIX  ░░░░░░░░░░░
░░░░░░░░░░  [ THE MATRIX HAS YOU... FOLLOW THE WHITE RABBIT ]  ░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"""
        
        # Create gradient effect
        lines = logo.split('\n')
        for i, line in enumerate(lines):
            if i < 2:
                style = colors["dim"]
            elif i < 5:
                style = colors["secondary"] 
            elif i < 8:
                style = colors["primary"]
            else:
                style = colors["success"]
            console.print(Text(line, style=style))
    
    def render_subtitle(self, console) -> None:
        """Render Matrix subtitle panel"""
        colors = self.get_colors()
        
        subtitle_text = Text()
        subtitle_text.append("≋ ", style=colors["accent"])
        subtitle_text.append("DIGITAL VALIDATION MATRIX", style=f"bold {colors['primary']}")
        subtitle_text.append(" ≋ ", style=colors["accent"])
        subtitle_text.append("NEURAL PROCESSING UNIT", style=colors["secondary"])
        subtitle_text.append(" ≋ ", style=colors["accent"])
        subtitle_text.append("v0.1101001", style=f"bold {colors['primary']}")
        subtitle_text.append(" ≋", style=colors["accent"])
        
        subtitle = Panel.fit(
            Align.center(subtitle_text),
            border_style=colors["border"],
            padding=(0, 1),
            title=f"[{colors['accent']}]▓ CONSTRUCT PROGRAM ACTIVE ▓[/{colors['accent']}]",
            title_align="center"
        )
        console.print(subtitle)
        console.print()
    
    def render_menu_item(self, name: str, desc: str, selected: bool) -> Text:
        """Render Matrix-style menu item"""
        colors = self.get_colors()
        
        if selected:
            style = colors["selected"]
            prefix = "▶ "
            suffix = " ◀"
            accent_style = colors["primary"]
        else:
            style = colors["primary"]
            prefix = "  "
            suffix = "  "
            accent_style = colors["dim"]
        
        menu_line = Text()
        menu_line.append("  ▓ ", style=accent_style)
        menu_line.append(f"{prefix}{name:<25}", style=style)
        menu_line.append(f"{desc}{suffix}", style=style if selected else colors["dim"])
        
        return menu_line
    
    def render_separator(self, title: str = "") -> Text:
        """Render Matrix section separator"""
        colors = self.get_colors()
        if title:
            separator = Text("  ▓ ", style=colors["success"]) + \
                       Text("≋" * 30 + f" ≋ {title} ≋ " + "≋" * 30, style=colors["success"])
        else:
            separator = Text("  ▓ ", style=colors["success"]) + \
                       Text("≋" * 70, style=colors["success"])
        return separator
    
    def render_footer(self, console) -> None:
        """Render Matrix control panel"""
        colors = self.get_colors()
        
        controls = Text()
        controls.append("≋ ", style=colors["accent"])
        controls.append("NEURAL INTERFACE", style=f"bold {colors['primary']}")
        controls.append(" ≋  ", style=colors["accent"])
        controls.append("↑↓", style=colors["success"])
        controls.append(" Jack In  ", style=colors["secondary"])
        controls.append("⟨ENTER⟩", style=colors["success"])
        controls.append(" Execute  ", style=colors["secondary"])
        controls.append("⟨ESC⟩", style=colors["warning"])
        controls.append(" Disconnect  ", style=colors["secondary"])
        controls.append("⟨MIND⟩", style=colors["accent"])
        controls.append(" Neural Link", style=colors["secondary"])
        
        footer = Panel.fit(
            Align.center(controls),
            border_style=colors["border"],
            title=f"[{colors['accent']}]▓ DIGITAL REALITY INTERFACE ▓[/{colors['accent']}]",
            title_align="center",
            padding=(0, 1)
        )
        console.print()
        console.print(footer)
    
    def get_loading_message(self) -> str:
        return "[dim]≋ Loading digital construct... ≋[/dim]"
    
    def get_execution_message(self, action: str) -> str:
        colors = self.get_colors()
        return f"[{colors['success']}]≋ EXECUTING:[/{colors['success']}] [{colors['primary']}]{action}[/{colors['primary']}]"
    
    def get_goodbye_message(self) -> str:
        colors = self.get_colors()
        return f"\n[{colors['primary']}]≋ Until we meet again in the construct... ≋[/{colors['primary']}]"