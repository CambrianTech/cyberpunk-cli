#!/usr/bin/env python3
"""
Loki Theme - Nordic mythology inspired terminal interface
Green and gold aesthetics with trickster god styling
"""

from .base_theme import BaseTheme
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from typing import Dict


class LokiTheme(BaseTheme):
    """Loki-inspired terminal theme with green and gold colors"""
    
    def __init__(self):
        super().__init__()
        self.name = "loki"
        self.description = "Nordic mythology terminal interface"
        
    def get_colors(self) -> Dict[str, str]:
        return {
            "primary": "bright_green",       # Loki's signature green
            "secondary": "green",            # Darker green
            "accent": "bright_yellow",       # Gold accents
            "background": "black",           # Terminal background
            "warning": "bright_red",         # Warning/error text
            "success": "bright_green",       # Success indicators
            "border": "green",               # Panel borders
            "selected": "black on bright_green",  # Selection highlight
            "dim": "color(28)",              # Dim green text
            "gold": "color(220)",            # Rich gold for special elements
        }
    
    def render_logo(self, console) -> None:
        """Render Loki-inspired logo"""
        colors = self.get_colors()
        
        logo = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║    ██╗      ██████╗ ██╗  ██╗██╗    ████████╗███████╗██████╗ ███╗   ███╗   ║
║    ██║     ██╔═══██╗██║ ██╔╝██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║   ║
║    ██║     ██║   ██║█████╔╝ ██║       ██║   █████╗  ██████╔╝██╔████╔██║   ║
║    ██║     ██║   ██║██╔═██╗ ██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║   ║
║    ███████╗╚██████╔╝██║  ██╗██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║   ║
║    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝   ║
║                                                                           ║
║  ████████████████████████████████████████████████████████████████████████ ║
║  █                   ASGARD TERMINAL SYSTEM v3.0                       █ ║
║  █                    [ TRICKSTER PROTOCOL ]                           █ ║
║  ████████████████████████████████████████████████████████████████████████ ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝"""
        
        console.print(Text(logo, style=colors["primary"]))
    
    def render_subtitle(self, console) -> None:
        """Render Loki subtitle panel"""
        colors = self.get_colors()
        
        subtitle_text = Text()
        subtitle_text.append("⚡ ", style=colors["gold"])
        subtitle_text.append("LOKI TERMINAL INTERFACE", style=f"bold {colors['primary']}")
        subtitle_text.append(" ⚡ ", style=colors["gold"])
        subtitle_text.append("SHAPE-SHIFTING PROTOCOLS", style=colors["secondary"])
        subtitle_text.append(" ⚡ ", style=colors["gold"])
        subtitle_text.append("Build 3.0", style=f"bold {colors['gold']}")
        subtitle_text.append(" ⚡", style=colors["gold"])
        
        subtitle = Panel.fit(
            Align.center(subtitle_text),
            border_style=colors["border"],
            padding=(0, 1),
            title=f"[{colors['gold']}]⟨ GOD OF MISCHIEF COMPUTING SYSTEM ⟩[/{colors['gold']}]",
            title_align="center"
        )
        console.print(subtitle)
        console.print()
    
    def render_menu_item(self, name: str, desc: str, selected: bool) -> Text:
        """Render Loki-style menu item"""
        colors = self.get_colors()
        
        if selected:
            style = colors["selected"]
            prefix = "→ "
            suffix = " ←"
            accent_style = colors["gold"]
        else:
            style = colors["primary"]
            prefix = "  "
            suffix = "  "
            accent_style = colors["dim"]
        
        menu_line = Text()
        menu_line.append("  ▶ ", style=accent_style)
        menu_line.append(f"{prefix}{name:<25}", style=style)
        menu_line.append(f"{desc}{suffix}", style=style if selected else colors["dim"])
        
        return menu_line
    
    def render_separator(self, title: str = "") -> Text:
        """Render Nordic-style section separator"""
        colors = self.get_colors()
        if title:
            separator = Text("  ▶ ", style=colors["gold"]) + \
                       Text("═" * 45 + f" ⚡ {title} ⚡ " + "═" * 15, style=colors["gold"])
        else:
            separator = Text("  ▶ ", style=colors["gold"]) + \
                       Text("═" * 70, style=colors["gold"])
        return separator
    
    def render_footer(self, console) -> None:
        """Render Loki control panel"""
        colors = self.get_colors()
        
        controls = Text()
        controls.append("⚡ ", style=colors["gold"])
        controls.append("TRICKSTER CONTROLS", style=f"bold {colors['primary']}")
        controls.append(" ⚡  ", style=colors["gold"])
        controls.append("↑↓", style=colors["gold"])
        controls.append(" Navigate  ", style=colors["secondary"])
        controls.append("[ENTER]", style=colors["gold"])
        controls.append(" Execute  ", style=colors["secondary"])
        controls.append("[ESC]", style=colors["warning"])
        controls.append(" Escape  ", style=colors["secondary"])
        controls.append("[CTRL+T]", style=colors["accent"])
        controls.append(" Transform", style=colors["secondary"])
        
        footer = Panel.fit(
            Align.center(controls),
            border_style=colors["border"],
            title=f"[{colors['gold']}]⟨ SHAPE-SHIFTER INTERFACE ⟩[/{colors['gold']}]",
            title_align="center",
            padding=(0, 1)
        )
        console.print()
        console.print(footer)
    
    def get_loading_message(self) -> str:
        return "[dim]⚡ SUMMONING LOKI INTERFACE ⚡[/dim]"
    
    def get_execution_message(self, action: str) -> str:
        colors = self.get_colors()
        return f"[{colors['gold']}]⚡ EXECUTING:[/{colors['gold']}] [{colors['primary']}]{action}[/{colors['primary']}]"
    
    def get_goodbye_message(self) -> str:
        colors = self.get_colors()
        return f"\n[{colors['primary']}]⚡ MISCHIEF MANAGED - LOKI OUT ⚡[/{colors['primary']}]"