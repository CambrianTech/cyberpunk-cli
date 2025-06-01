# Cyberpunk CLI

<div align="center">

```
   ╔═══════════════════════════════════════════════════╗
   ║                 CYBERPUNK CLI                     ║
   ║              Terminal Interface                   ║
   ║                  Framework                        ║
   ╚═══════════════════════════════════════════════════╝
```

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/Cambrian/cyberpunk-cli)

**[TRY LIVE DEMO](https://cambrian.github.io/cyberpunk-cli/)**

</div>

**Professional cyberpunk-themed terminal interface framework for Python CLI applications. Transform any Click-based CLI into a retro-futuristic terminal experience with zero effort.**

## Features

### Zero-Effort Enhancement
```python
import cyberpunk_cli  # Just add this line
import click

@click.command()
def main():
    """Your existing CLI"""
    pass
```

### Full Framework
```python
from cyberpunk_cli import cyberpunk, option

@cyberpunk(theme="loki", theme_switching=True)
@option('--deploy', help='Deploy to production')
def main(deploy):
    """Professional CLI with cyberpunk interface"""
    pass
```

### Core Features
- **Multiple Retro Themes** - Loki, Matrix, Fallout, Tron aesthetics
- **Full Mouse Support** - Click to select, double-click to execute  
- **Keyboard Navigation** - Arrow keys, Enter, numbers, ESC
- **Responsive Design** - Adapts to terminal size
- **Modern UX** - Smooth animations and visual feedback
- **Easy Integration** - Simple, fluent API
- **Click Integration** - Auto-enhance existing Click applications

## Quick Start

### Installation

```bash
pip install cyberpunk-cli
```

### Basic Usage

```python
from cyberpunk_cli import CyberpunkMenu

# Create menu with Loki theme (default)
menu = CyberpunkMenu("My Application", theme="loki")

# Add options with fluent interface
menu.add_option("deploy", "Deploy", "Deploy to production") \
    .add_option("test", "Test", "Run test suite") \
    .add_option("build", "Build", "Build application") \
    .add_separator() \
    .add_exit()

# Run and get selection
choice = menu.run()

if choice == "deploy":
    print("Deploying application...")
elif choice == "test":
    print("Running tests...")
```

## Available Themes

### Loki Theme (Default)
Green and gold terminal aesthetics with Nordic mythology styling.

### Matrix Theme  
Digital rain aesthetic with green code and neural network terminology.

### Fallout Theme
Vault-Tec terminal interface with amber colors and retro-futuristic styling.

### Tron Theme
Neon blue cyberpunk grid with light cycle inspired design.

## Input Methods

- **Arrow Keys** - Navigate up/down through options
- **Enter** - Execute selected option
- **Numbers** - Direct selection (0-9)
- **Mouse Click** - Click any option to select it
- **Mouse Double-Click** - Double-click to execute immediately
- **Ctrl+T** - Quick theme switcher
- **ESC/Q** - Exit the menu

## Advanced Usage

### Command Groups
```python
from cyberpunk_cli import cyberpunk, group, option

@group()
def cli():
    """Main CLI group"""
    pass

@cli.command()
@option('--env', help='Environment to deploy')
def deploy(env):
    """Deploy application"""
    print(f"Deploying to {env}")

@cli.command() 
def status():
    """Check application status"""
    print("System operational")

if __name__ == "__main__":
    cyberpunk.enhance_group(cli)
```

### Theme Control
```python
# Set default theme, allow user switching
@cyberpunk(theme="loki", theme_switching=True)

# Lock theme, prevent user changes  
@cyberpunk(theme="matrix", theme_switching=False)

# Use saved preference
@cyberpunk(theme_switching=True)
```

### Click Integration

#### Automatic Enhancement
Any existing Click application can be enhanced by simply importing cyberpunk_cli:

```python
import cyberpunk_cli  # Automatically enhances Click commands
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--verbose', is_flag=True)
def process(verbose):
    """Process data"""
    pass
```

#### Manual Enhancement
```python
from cyberpunk_cli import enhance_click_app
import click

@click.command()
def original_cli():
    """Original Click CLI"""
    pass

# Enhance existing Click command
enhanced_cli = enhance_click_app(original_cli, theme="loki")
```

## Examples

### DevOps Tool
```python
from cyberpunk_cli import cyberpunk, option

@cyberpunk(theme="loki")
@option('--env', help='Target environment')
@option('--force', is_flag=True, help='Force deployment')
def deploy(env, force):
    """Deploy to specified environment"""
    if force:
        print(f"Force deploying to {env}")
    else:
        print(f"Deploying to {env}")
```

### Development Console
```python
from cyberpunk_cli import cyberpunk

@cyberpunk(theme="matrix", theme_switching=False)
def debug_console():
    """Development debug console"""
    print("Debug console initialized")
    print("System diagnostics running...")
```

## API Reference

### Decorators
- `@cyberpunk` - Main decorator for CLI enhancement
- `@option` - Command option definition
- `@group` - Command group definition

### Functions
- `enhance_click_app()` - Enhance existing Click applications
- `set_global_theme()` - Set theme globally
- `get_theme_list()` - List available themes

### Classes
- `CyberpunkMenu` - Menu interface class
- `CyberpunkConfig` - Configuration management
- `ThemeManager` - Theme switching and persistence

## Configuration

### Global Configuration
```json
{
  "theme": "loki",
  "mouse_support": true,
  "animations": true,
  "compact_mode": false
}
```

### Project Configuration
```json
{
  "theme": "matrix",
  "custom_title": "My App v2.0"
}
```

## Use Cases

Perfect for:
- **DevOps Tools** - Deployment, monitoring, CI/CD interfaces
- **Game Development** - In-game terminals, debug menus
- **System Administration** - Server management, diagnostics
- **Data Science** - Model training, analysis tool selection
- **Creative Tools** - Asset pipelines, rendering farms
- **Research Applications** - Experiment runners, data processors

## Requirements

- Python 3.8 or higher
- Rich terminal library
- Click framework
- Modern terminal with mouse support

## Contributing

Contributions welcome. Please read CONTRIBUTING.md for guidelines.

### Development Setup

```bash
git clone https://github.com/Cambrian/cyberpunk-cli.git
cd cyberpunk-cli
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
black cyberpunk_cli/
flake8 cyberpunk_cli/
```

## License

MIT License - see LICENSE file for details.

## Related Projects

- [Rich](https://github.com/Textualize/rich) - Rich text and beautiful formatting
- [Click](https://github.com/pallets/click) - Command line interface creation kit
- [Inquirer](https://github.com/magmax/python-inquirer) - Collection of common interactive command line user interfaces

---

<div align="center">

**Cyberpunk CLI Framework**  
*Professional terminal interfaces for the digital age*

Built by **Cambrian**

</div>