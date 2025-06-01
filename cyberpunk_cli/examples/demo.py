#!/usr/bin/env python3
"""
Cyberpunk CLI Demo - Showcase all themes and features

This demo shows off all the cyberpunk menu themes and features:
- Multiple retro themes (Fallout, Matrix, Tron)
- Mouse support (click to select, double-click to execute)
- Keyboard navigation (arrows, enter, numbers)
- Responsive layout
"""

import sys
from ..menu import CyberpunkMenu
from ..themes import theme_manager


def show_theme_selector():
    """Show theme selection menu"""
    print("🎨 Select a theme to demo:")
    print("1. Fallout (Vault-Tec)")
    print("2. Matrix (Digital Rain)")
    print("3. Tron (Neon Grid)")
    print("4. All Themes")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        return ["fallout"]
    elif choice == "2":
        return ["matrix"]
    elif choice == "3":
        return ["tron"]
    elif choice == "4":
        return ["fallout", "matrix", "tron"]
    else:
        return ["fallout"]  # Default


def create_demo_menu(theme_name: str) -> CyberpunkMenu:
    """Create a demo menu with sample options"""
    menu = CyberpunkMenu(f"Cyberpunk CLI Demo - {theme_name.title()} Theme", theme_name)
    
    # Add sample options
    menu.add_option("deploy", "🚀 Deploy", "Deploy application to production")
    menu.add_option("test", "🧪 Run Tests", "Execute comprehensive test suite")
    menu.add_option("build", "🔨 Build", "Compile and package application")
    menu.add_option("docs", "📚 Documentation", "Generate and view documentation")
    
    menu.add_separator()
    
    menu.add_option("config", "⚙️ Configuration", "Modify application settings")
    menu.add_option("logs", "📊 View Logs", "Display application logs")
    menu.add_option("monitor", "📈 Monitor", "Real-time system monitoring")
    
    menu.add_separator()
    
    menu.add_exit("❌ Exit Demo", "Return to theme selection")
    
    return menu


def run_demo():
    """Run the cyberpunk CLI demo"""
    print("🔥 CYBERPUNK CLI DEMO 🔥")
    print("Professional terminal menus with retro aesthetics")
    print()
    
    while True:
        themes = show_theme_selector()
        
        for theme_name in themes:
            if not theme_manager.set_theme(theme_name):
                print(f"❌ Theme '{theme_name}' not available")
                continue
                
            print(f"\n🎨 Loading {theme_name.title()} theme...")
            
            menu = create_demo_menu(theme_name)
            
            while True:
                choice = menu.run()
                
                if choice is None:  # Exit
                    break
                elif choice == "deploy":
                    print("🚀 Deploying application...")
                    input("Press Enter to continue...")
                elif choice == "test":
                    print("🧪 Running tests...")
                    input("Press Enter to continue...")
                elif choice == "build":
                    print("🔨 Building application...")
                    input("Press Enter to continue...")
                elif choice == "docs":
                    print("📚 Generating documentation...")
                    input("Press Enter to continue...")
                elif choice == "config":
                    print("⚙️ Opening configuration...")
                    input("Press Enter to continue...")
                elif choice == "logs":
                    print("📊 Displaying logs...")
                    input("Press Enter to continue...")
                elif choice == "monitor":
                    print("📈 Starting monitor...")
                    input("Press Enter to continue...")
                else:
                    print(f"Unknown option: {choice}")
                    input("Press Enter to continue...")
            
            if len(themes) > 1:
                print(f"\n✅ {theme_name.title()} theme demo complete!")
                input("Press Enter for next theme...")
        
        print("\n🎉 Demo complete!")
        again = input("Run demo again? (y/N): ").strip().lower()
        if again != 'y':
            break
    
    print("👋 Thanks for trying Cyberpunk CLI!")


def main():
    """Main entry point for demo"""
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"❌ Demo error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()