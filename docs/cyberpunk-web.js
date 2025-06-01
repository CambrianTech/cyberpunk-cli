/**
 * Cyberpunk CLI Web Framework
 * Create terminal interfaces for websites that match the Python package themes
 */

class CyberpunkTerminal {
    constructor(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        this.theme = options.theme || 'loki';
        this.title = options.title || 'Cyberpunk Terminal';
        this.themeChanging = options.themeChanging !== false;
        this.mouseSupport = options.mouseSupport !== false;
        this.keyboardShortcuts = options.keyboardShortcuts !== false;
        
        this.menuItems = [];
        this.selectedIndex = 0;
        this.output = [];
        this.themeConfig = null;
        
        this.loadThemeConfig().then(() => this.init());
    }
    
    async loadThemeConfig() {
        try {
            // Try to load from the same source as Python
            const response = await fetch('themes/theme_config.json');
            this.themeConfig = await response.json();
        } catch (error) {
            // Fallback to embedded config
            this.themeConfig = this.getEmbeddedThemeConfig();
        }
    }
    
    getEmbeddedThemeConfig() {
        // Embedded version of the theme config for when JSON file isn't available
        return {
            "themes": {
                "loki": {
                    "display_name": "Loki",
                    "terminology": {
                        "system_name": "ASGARD TERMINAL SYSTEM",
                        "version": "v3.0"
                    }
                },
                "matrix": {
                    "display_name": "Matrix", 
                    "terminology": {
                        "system_name": "NEURAL MATRIX TERMINAL",
                        "version": "v1.0"
                    }
                },
                "fallout": {
                    "display_name": "Fallout",
                    "terminology": {
                        "system_name": "VAULT-TEC TERMINAL", 
                        "version": "v2.077"
                    }
                },
                "tron": {
                    "display_name": "Tron",
                    "terminology": {
                        "system_name": "TRON GRID TERMINAL",
                        "version": "v2.0"
                    }
                }
            }
        };
    }
    
    init() {
        this.container.className = `cyberpunk-terminal cyberpunk-theme-${this.theme}`;
        this.setupKeyboardShortcuts();
        this.render();
    }
    
    setTheme(theme) {
        this.theme = theme;
        this.container.className = `cyberpunk-terminal cyberpunk-theme-${theme}`;
        this.log(`Theme switched to ${theme.charAt(0).toUpperCase() + theme.slice(1)}`);
    }
    
    addMenuItem(key, name, description, action) {
        this.menuItems.push({ key, name, description, action });
        this.render();
        return this;
    }
    
    addSeparator(title = '') {
        this.menuItems.push({ type: 'separator', title });
        this.render();
        return this;
    }
    
    setTitle(title) {
        this.title = title;
        this.render();
        return this;
    }
    
    log(message) {
        this.output.push(`<div>${message}</div>`);
        this.updateOutput();
    }
    
    clear() {
        this.output = [];
        this.updateOutput();
    }
    
    executeCommand(command) {
        this.log(`> ${command}`);
        // Execute command logic here
    }
    
    render() {
        const themes = this.themeChanging ? this.renderThemeSelector() : '';
        
        this.container.innerHTML = `
            ${themes}
            
            <div class="cyberpunk-header">
                <div class="cyberpunk-logo">${this.getLogo()}</div>
                <div class="cyberpunk-subtitle">
                    ${this.getSubtitle()}
                </div>
            </div>
            
            <div class="cyberpunk-menu">
                ${this.renderMenu()}
            </div>
            
            <div class="cyberpunk-output" id="cyberpunk-output">
                ${this.output.join('')}
                <div><span class="cyberpunk-cursor"></span></div>
            </div>
            
            <div class="cyberpunk-footer">
                ${this.getFooterText()}
            </div>
        `;
        
        this.attachEventListeners();
    }
    
    renderThemeSelector() {
        return `
            <div class="cyberpunk-theme-selector">
                <div style="margin-bottom: 10px; font-weight: bold;">THEMES [CTRL+T]</div>
                <button class="cyberpunk-btn" onclick="window.cyberpunkTerminal.setTheme('loki')">Loki</button>
                <button class="cyberpunk-btn" onclick="window.cyberpunkTerminal.setTheme('matrix')">Matrix</button>
                <button class="cyberpunk-btn" onclick="window.cyberpunkTerminal.setTheme('fallout')">Fallout</button>
                <button class="cyberpunk-btn" onclick="window.cyberpunkTerminal.setTheme('tron')">Tron</button>
            </div>
        `;
    }
    
    renderMenu() {
        return this.menuItems.map((item, index) => {
            if (item.type === 'separator') {
                return `<div class="cyberpunk-separator">${'═'.repeat(70)} ${item.title} ${'═'.repeat(20)}</div>`;
            }
            
            const isSelected = index === this.selectedIndex;
            const selectedClass = isSelected ? 'selected' : '';
            
            return `
                <div class="cyberpunk-menu-item ${selectedClass}" 
                     onclick="window.cyberpunkTerminal.selectItem(${index})"
                     data-index="${index}">
                    <span>▶ ${item.name}</span>
                    <span>${item.description}</span>
                </div>
            `;
        }).join('');
    }
    
    selectItem(index) {
        this.selectedIndex = index;
        const item = this.menuItems[index];
        
        if (item && item.action) {
            this.log(`Executing: ${item.name}`);
            if (typeof item.action === 'function') {
                item.action();
            } else if (typeof item.action === 'string') {
                this.executeCommand(item.action);
            }
        }
        
        this.render();
    }
    
    updateOutput() {
        const outputEl = document.getElementById('cyberpunk-output');
        if (outputEl) {
            outputEl.innerHTML = this.output.join('') + '<div><span class="cyberpunk-cursor"></span></div>';
        }
    }
    
    attachEventListeners() {
        // Store reference for global access
        window.cyberpunkTerminal = this;
    }
    
    setupKeyboardShortcuts() {
        if (!this.keyboardShortcuts) return;
        
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 't' && this.themeChanging) {
                e.preventDefault();
                this.cycleTheme();
            }
            
            if (e.key === 'ArrowUp') {
                e.preventDefault();
                this.selectedIndex = Math.max(0, this.selectedIndex - 1);
                this.render();
            }
            
            if (e.key === 'ArrowDown') {
                e.preventDefault();
                this.selectedIndex = Math.min(this.menuItems.length - 1, this.selectedIndex + 1);
                this.render();
            }
            
            if (e.key === 'Enter') {
                e.preventDefault();
                this.selectItem(this.selectedIndex);
            }
        });
    }
    
    cycleTheme() {
        const themes = ['loki', 'matrix', 'fallout', 'tron'];
        const currentIndex = themes.indexOf(this.theme);
        const nextIndex = (currentIndex + 1) % themes.length;
        this.setTheme(themes[nextIndex]);
    }
    
    getLogo() {
        const logos = {
            loki: `╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║    ██╗      ██████╗ ██╗  ██╗██╗    ████████╗███████╗██████╗ ███╗   ███╗   ║
║    ██║     ██╔═══██╗██║ ██╔╝██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║   ║
║    ██║     ██║   ██║█████╔╝ ██║       ██║   █████╗  ██████╔╝██╔████╔██║   ║
║    ██║     ██║   ██║██╔═██╗ ██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║   ║
║    ███████╗╚██████╔╝██║  ██╗██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║   ║
║    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝`,
            
            matrix: `╔═══════════════════════════════════════════════════════════════════════════╗
║  ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗    ████████╗███████╗██████╗  ║
║  ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝    ╚══██╔══╝██╔════╝██╔══██╗ ║
║  ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝        ██║   █████╗  ██████╔╝ ║
║  ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗        ██║   ██╔══╝  ██╔══██╗ ║
║  ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗       ██║   ███████╗██║  ██║ ║
║  ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝ ║
╚═══════════════════════════════════════════════════════════════════════════╝`,
            
            fallout: `╔═══════════════════════════════════════════════════════════════════════════╗
║    █████████╗███╗   ███╗ █████╗ ██████╗ ████████╗      ██████╗██╗         ║
║    ██╔══════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝     ██╔════╝██║         ║
║    ███████╗ ██╔████╔██║███████║██████╔╝   ██║  █████╗██║     ██║         ║
║    ╚════██║ ██║╚██╔╝██║██╔══██║██╔══██╗   ██║  ╚════╝██║     ██║         ║
║    ███████║ ██║ ╚═╝ ██║██║  ██║██║  ██║   ██║        ╚██████╗██║         ║
║    ╚══════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝         ╚═════╝╚═╝         ║
╚═══════════════════════════════════════════════════════════════════════════╝`,
            
            tron: `╔═══════════════════════════════════════════════════════════════════════════╗
║  ████████╗██████╗  ██████╗ ███╗   ██╗    ████████╗███████╗██████╗ ███╗   ███╗ ║
║  ╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║ ║
║     ██║   ██████╔╝██║   ██║██╔██╗ ██║       ██║   █████╗  ██████╔╝██╔████╔██║ ║
║     ██║   ██╔══██╗██║   ██║██║╚██╗██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║ ║
║     ██║   ██║  ██║╚██████╔╝██║ ╚████║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║ ║
║     ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ║
╚═══════════════════════════════════════════════════════════════════════════╝`
        };
        
        return logos[this.theme] || logos.loki;
    }
    
    getSubtitle() {
        const subtitles = {
            loki: '⚡ LOKI TERMINAL INTERFACE ⚡ SHAPE-SHIFTING PROTOCOLS ⚡ Web Framework ⚡',
            matrix: '▦ MATRIX TERMINAL INTERFACE ▦ NEURAL NETWORK PROTOCOLS ▦ Web Framework ▦',
            fallout: '*** VAULT-TEC TERMINAL INTERFACE *** AUTOMATED SYSTEMS *** Web Framework ***',
            tron: '◊ TRON TERMINAL INTERFACE ◊ LIGHT CYCLE PROTOCOLS ◊ Web Framework ◊'
        };
        
        return subtitles[this.theme] || subtitles.loki;
    }
    
    getFooterText() {
        const footers = {
            loki: '⚡ Navigation: Mouse Click | Theme Switch: Ctrl+T | Built for Web ⚡',
            matrix: '▦ Navigation: Mouse Click | Theme Switch: Ctrl+T | Built for Web ▦',
            fallout: '*** Navigation: Mouse Click | Theme Switch: Ctrl+T | Built for Web ***',
            tron: '◊ Navigation: Mouse Click | Theme Switch: Ctrl+T | Built for Web ◊'
        };
        
        return footers[this.theme] || footers.loki;
    }
}

// Simple Console Widget
class CyberpunkConsole {
    constructor(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        this.theme = options.theme || 'loki';
        this.title = options.title || 'Cyberpunk Console';
        this.output = [];
        this.history = [];
        this.historyIndex = -1;
        
        this.init();
    }
    
    init() {
        this.container.className = `cyberpunk-console cyberpunk-theme-${this.theme}`;
        this.render();
    }
    
    render() {
        this.container.innerHTML = `
            <div class="cyberpunk-console-header">
                <div class="cyberpunk-console-title">${this.title}</div>
                <div class="cyberpunk-console-controls">
                    <button class="cyberpunk-btn" onclick="this.parentNode.parentNode.parentNode.cyberpunkConsole.clear()">Clear</button>
                </div>
            </div>
            <div class="cyberpunk-console-body" id="console-body-${this.container.id}">
                ${this.output.join('')}
                <div>
                    <span>$ </span>
                    <input type="text" class="cyberpunk-input" 
                           placeholder="Enter command..." 
                           onkeydown="this.parentNode.parentNode.parentNode.cyberpunkConsole.handleInput(event)">
                </div>
            </div>
        `;
        
        this.container.cyberpunkConsole = this;
    }
    
    log(message, type = 'output') {
        const timestamp = new Date().toLocaleTimeString();
        this.output.push(`<div class="console-${type}">[${timestamp}] ${message}</div>`);
        this.updateOutput();
    }
    
    clear() {
        this.output = [];
        this.updateOutput();
    }
    
    executeCommand(command) {
        this.history.push(command);
        this.historyIndex = this.history.length;
        this.log(`$ ${command}`, 'input');
        
        // Basic command processing
        if (command === 'clear') {
            this.clear();
        } else if (command === 'help') {
            this.log('Available commands: clear, help, theme [name]');
        } else if (command.startsWith('theme ')) {
            const theme = command.split(' ')[1];
            this.setTheme(theme);
        } else {
            this.log(`Command not found: ${command}`, 'error');
        }
    }
    
    setTheme(theme) {
        this.theme = theme;
        this.container.className = `cyberpunk-console cyberpunk-theme-${theme}`;
        this.log(`Theme changed to ${theme}`);
    }
    
    handleInput(event) {
        if (event.key === 'Enter') {
            const command = event.target.value.trim();
            if (command) {
                this.executeCommand(command);
                event.target.value = '';
            }
        }
        
        if (event.key === 'ArrowUp') {
            if (this.historyIndex > 0) {
                this.historyIndex--;
                event.target.value = this.history[this.historyIndex];
            }
        }
        
        if (event.key === 'ArrowDown') {
            if (this.historyIndex < this.history.length - 1) {
                this.historyIndex++;
                event.target.value = this.history[this.historyIndex];
            } else {
                this.historyIndex = this.history.length;
                event.target.value = '';
            }
        }
    }
    
    updateOutput() {
        const body = document.getElementById(`console-body-${this.container.id}`);
        if (body) {
            body.innerHTML = this.output.join('') + `
                <div>
                    <span>$ </span>
                    <input type="text" class="cyberpunk-input" 
                           placeholder="Enter command..." 
                           onkeydown="this.parentNode.parentNode.parentNode.cyberpunkConsole.handleInput(event)">
                </div>
            `;
            body.scrollTop = body.scrollHeight;
        }
    }
}

// Export for module use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { CyberpunkTerminal, CyberpunkConsole };
}