# 🔥 Cyberpunk CLI

**Professional terminal menu system with retro cyberpunk aesthetics**

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Rich](https://img.shields.io/badge/rich-terminal-ff69b4.svg)

A powerful, themeable terminal menu library inspired by retro-futuristic interfaces from Fallout, The Matrix, and Tron. Create stunning cyberpunk-styled CLI applications with full mouse support, responsive layouts, and multiple input methods.

## ✨ Features

- 🎨 **Multiple Retro Themes** - Fallout, Matrix, Tron aesthetics
- 🖱️ **Full Mouse Support** - Click to select, double-click to execute  
- ⌨️ **Keyboard Navigation** - Arrow keys, Enter, numbers, ESC
- 📱 **Responsive Design** - Adapts to terminal size
- 🎮 **Modern UX** - Smooth animations and visual feedback
- 🔧 **Easy Integration** - Simple, fluent API
- 🎯 **Zero Dependencies** - Only requires `rich`

## 🚀 Quick Start

### Installation

```bash
pip install cyberpunk-cli
```

### Basic Usage

```python
from cyberpunk_cli import CyberpunkMenu

# Create menu with Fallout theme
menu = CyberpunkMenu("My Application", theme="fallout")

# Add options with fluent interface
menu.add_option("deploy", "🚀 Deploy", "Deploy to production") \\
    .add_option("test", "🧪 Test", "Run test suite") \\
    .add_option("build", "🔨 Build", "Build application") \\
    .add_separator() \\
    .add_exit()

# Run and get selection
choice = menu.run()

if choice == "deploy":
    print("Deploying application...")
elif choice == "test":
    print("Running tests...")
```

## 🎨 Available Themes

### 🏚️ Fallout Theme
Vault-Tec terminal interface with amber colors and retro-futuristic styling.

### 💚 Matrix Theme  
Digital rain aesthetic with green code and neural network terminology.

### 💙 Tron Theme
Neon blue cyberpunk grid with light cycle inspired design.

## 🖱️ Input Methods

- **Arrow Keys** - Navigate up/down through options
- **Enter** - Execute selected option
- **Numbers** - Direct selection (0-9)
- **Mouse Click** - Click any option to select it
- **Mouse Double-Click** - Double-click to execute immediately
- **ESC/Q** - Exit the menu

## 📋 Advanced Usage

### Custom Options and Separators

```python
from cyberpunk_cli import CyberpunkMenu

menu = CyberpunkMenu("Advanced Demo", theme="matrix")

# Add grouped options
menu.add_option("new", "📄 New File", "Create a new file") \\
    .add_option("open", "📂 Open", "Open existing file") \\
    .add_option("save", "💾 Save", "Save current file") \\
    .add_separator() \\
    .add_option("settings", "⚙️ Settings", "Configure application") \\
    .add_option("help", "❓ Help", "Show help documentation") \\
    .add_exit("🚪 Quit", "Exit application")

choice = menu.run()
```

### Theme Switching

```python
from cyberpunk_cli import theme_manager, CyberpunkMenu

# List available themes
themes = theme_manager.list_themes()
print(f"Available themes: {themes}")

# Switch theme
theme_manager.set_theme("tron")

# Create menu with new theme
menu = CyberpunkMenu("Tron Interface")
```

### Creating Custom Themes

```python
from cyberpunk_cli import BaseTheme
from rich.text import Text
from rich.panel import Panel

class CustomTheme(BaseTheme):
    def __init__(self):
        super().__init__()
        self.name = "custom"
        self.description = "My custom theme"
    
    def get_colors(self):
        return {
            "primary": "purple",
            "secondary": "magenta", 
            "accent": "white",
            # ... more colors
        }
    
    def render_logo(self, console):
        logo = "MY CUSTOM LOGO"
        console.print(Text(logo, style="bold purple"))
    
    # Implement other required methods...

# Register custom theme
from cyberpunk_cli import theme_manager
theme_manager.register_theme(CustomTheme())
```

## 🎮 Demo

Try the interactive demo to see all themes and features:

```bash
cyberpunk-demo
```

Or run the demo programmatically:

```python
from cyberpunk_cli.examples.demo import main
main()
```

## 🔧 API Reference

### CyberpunkMenu

Main menu class with fluent interface.

#### Constructor
```python
CyberpunkMenu(title: str = "Cyberpunk Menu", theme: str = "fallout")
```

#### Methods
- `add_option(key, name, description)` - Add menu option
- `add_separator()` - Add visual separator  
- `add_exit(name, description)` - Add exit option
- `run()` - Display menu and return selected key

### Theme Manager

Global theme management.

```python
from cyberpunk_cli import theme_manager

theme_manager.set_theme("matrix")          # Switch theme
theme_manager.get_theme()                  # Get current theme
theme_manager.list_themes()                # List available themes
theme_manager.register_theme(custom_theme) # Add custom theme
```

## 🎯 Use Cases

Perfect for:
- 🚀 **DevOps Tools** - Deployment, monitoring, CI/CD interfaces
- 🎮 **Game Development** - In-game terminals, debug menus
- 🔧 **System Administration** - Server management, diagnostics
- 📊 **Data Science** - Model training, analysis tool selection
- 🎨 **Creative Tools** - Asset pipelines, rendering farms
- 🔬 **Research Applications** - Experiment runners, data processors

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/CambrianTech/cyberpunk-cli.git
cd cyberpunk-cli
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
black cyberpunk_cli/
flake8 cyberpunk_cli/
```

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

## 🔗 Related Projects

- [Rich](https://github.com/Textualize/rich) - Rich text and beautiful formatting
- [Click](https://github.com/pallets/click) - Command line interface creation kit
- [Inquirer](https://github.com/magmax/python-inquirer) - Collection of common interactive command line user interfaces

---

**Built with ❤️ by [CambrianTech](https://github.com/CambrianTech)**

*Bringing retro-futuristic aesthetics to modern terminal interfaces*