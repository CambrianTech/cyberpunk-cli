# Cyberpunk CLI

Professional terminal interface framework with retro-futuristic themes.

**[Try the Live Demo →](https://cambriantech.github.io/cyberpunk-cli/)**

## Quick Start

```bash
pip install cyberpunk-cli
```

```python
from cyberpunk_cli import CyberpunkMenu

menu = CyberpunkMenu("My App")
menu.add_option("deploy", "Deploy", "Deploy to production")
menu.add_option("test", "Test", "Run test suite") 
menu.add_exit()

choice = menu.run()
```

## Features

- **4 retro themes** - Loki, Matrix, Fallout, Tron
- **Mouse support** - Click to select, double-click to execute
- **Keyboard navigation** - Arrow keys, Enter, numbers
- **Theme switching** - Ctrl+T to cycle themes
- **Click integration** - Works with existing Click CLIs

## Themes

### Loki (default)
Green/gold Norse mythology aesthetic with Asgardian terminal styling.

### Matrix  
Digital rain with green code and neural network terminology.

### Fallout
Vault-Tec amber terminal with retro-futuristic post-apocalyptic design.

### Tron
Neon blue cyberpunk grid with light cycle inspired interface.

## API

### Basic Menu
```python
from cyberpunk_cli import CyberpunkMenu

menu = CyberpunkMenu("App Name", theme="matrix")
menu.add_option("id", "Display Name", "Description")
menu.add_separator()
menu.add_exit("Quit", "Exit application")

choice = menu.run()
```

### Click Integration
```python
from cyberpunk_cli import theme_manager
import click

# Auto-enhance any Click CLI
theme_manager.set_theme("loki")

@click.command()
@click.option('--env', help='Environment')  
def deploy(env):
    print(f"Deploying to {env}")
```

### Theme Control
```python
from cyberpunk_cli import theme_manager

# Set theme
theme_manager.set_theme("fallout")

# List available themes
themes = theme_manager.list_themes()
# ['loki', 'matrix', 'fallout', 'tron']
```

## Usage

### Navigation
- **↑↓** Navigate options
- **Enter** Execute selected
- **1-9** Direct selection  
- **Click** Select option
- **Double-click** Execute immediately
- **Ctrl+T** Switch themes
- **ESC/Q** Exit

### Input Methods
All input methods work simultaneously - use whatever feels natural.

## Requirements

- Python 3.8+
- Modern terminal with mouse support
- Rich and Click libraries (auto-installed)

## License

MIT License - see LICENSE file.

---

Built by [Cambrian](https://github.com/CambrianTech)