#!/usr/bin/env python3
"""
Browser automation tool for testing cyberpunk-cli web demos
Allows taking screenshots and getting rendered content for debugging
"""

import os
import sys
import time
import base64
from pathlib import Path
from typing import Optional, Dict, Any
import subprocess
import tempfile

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False


class BrowserTester:
    """Test cyberpunk-cli demos in real browsers"""
    
    def __init__(self, browser_type: str = "chrome", headless: bool = False):
        self.browser_type = browser_type.lower()
        self.headless = headless
        self.driver = None
        self.playwright = None
        self.page = None
        
    def start_selenium(self):
        """Start Selenium WebDriver"""
        if not SELENIUM_AVAILABLE:
            raise ImportError("Selenium not available. Install with: pip install selenium")
            
        if self.browser_type == "chrome":
            options = ChromeOptions()
            if self.headless:
                options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            self.driver = webdriver.Chrome(options=options)
        elif self.browser_type == "firefox":
            options = FirefoxOptions()
            if self.headless:
                options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unsupported browser: {self.browser_type}")
    
    def start_playwright(self):
        """Start Playwright browser"""
        if not PLAYWRIGHT_AVAILABLE:
            raise ImportError("Playwright not available. Install with: pip install playwright")
            
        self.playwright = sync_playwright().start()
        
        if self.browser_type == "chrome":
            browser = self.playwright.chromium.launch(headless=self.headless)
        elif self.browser_type == "firefox":
            browser = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_type == "safari":
            browser = self.playwright.webkit.launch(headless=self.headless)
        else:
            browser = self.playwright.chromium.launch(headless=self.headless)
            
        self.page = browser.new_page()
    
    def start(self, engine: str = "playwright"):
        """Start browser automation"""
        if engine == "playwright":
            self.start_playwright()
        elif engine == "selenium":
            self.start_selenium()
        else:
            raise ValueError(f"Unknown engine: {engine}")
    
    def navigate_to(self, url: str):
        """Navigate to URL"""
        if self.driver:
            self.driver.get(url)
        elif self.page:
            self.page.goto(url)
    
    def wait_for_element(self, selector: str, timeout: int = 10):
        """Wait for element to be present"""
        if self.driver:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
        elif self.page:
            return self.page.wait_for_selector(selector, timeout=timeout * 1000)
    
    def click_element(self, selector: str):
        """Click an element"""
        if self.driver:
            element = self.driver.find_element(By.CSS_SELECTOR, selector)
            element.click()
        elif self.page:
            self.page.click(selector)
    
    def get_text(self, selector: str) -> str:
        """Get text content of element"""
        if self.driver:
            element = self.driver.find_element(By.CSS_SELECTOR, selector)
            return element.text
        elif self.page:
            return self.page.text_content(selector) or ""
    
    def take_screenshot(self, filename: str = None) -> str:
        """Take screenshot and save to file"""
        if not filename:
            timestamp = int(time.time())
            filename = f"screenshot_{timestamp}.png"
        
        if self.driver:
            self.driver.save_screenshot(filename)
        elif self.page:
            self.page.screenshot(path=filename)
            
        return filename
    
    def get_console_logs(self) -> list:
        """Get browser console logs"""
        logs = []
        
        if self.driver:
            for log in self.driver.get_log('browser'):
                logs.append({
                    'level': log['level'],
                    'message': log['message'],
                    'timestamp': log['timestamp']
                })
        elif self.page:
            # Playwright console logs need to be set up during page creation
            pass
            
        return logs
    
    def execute_script(self, script: str):
        """Execute JavaScript in browser"""
        if self.driver:
            return self.driver.execute_script(script)
        elif self.page:
            return self.page.evaluate(script)
    
    def get_page_source(self) -> str:
        """Get rendered HTML source"""
        if self.driver:
            return self.driver.page_source
        elif self.page:
            return self.page.content()
        return ""
    
    def test_cyberpunk_demo(self, demo_url: str) -> Dict[str, Any]:
        """Test the cyberpunk CLI demo site"""
        results = {
            "url": demo_url,
            "status": "unknown",
            "errors": [],
            "screenshots": [],
            "themes_tested": [],
            "console_logs": []
        }
        
        try:
            # Navigate to demo
            self.navigate_to(demo_url)
            
            # Wait for page to load
            self.wait_for_element(".cyberpunk-terminal", timeout=10)
            
            # Take initial screenshot
            screenshot = self.take_screenshot("demo_initial.png")
            results["screenshots"].append(screenshot)
            
            # Test theme switching
            themes = ["loki", "matrix", "fallout", "tron"]
            for theme in themes:
                try:
                    # Click theme button
                    self.click_element(f'button[onclick*="{theme}"]')
                    time.sleep(1)  # Wait for theme to apply
                    
                    # Take screenshot
                    screenshot = self.take_screenshot(f"demo_theme_{theme}.png")
                    results["screenshots"].append(screenshot)
                    results["themes_tested"].append(theme)
                    
                except Exception as e:
                    results["errors"].append(f"Theme {theme} failed: {str(e)}")
            
            # Test menu interactions
            try:
                # Click a menu item
                self.click_element(".cyberpunk-menu-item:first-child")
                time.sleep(1)
                
                # Take screenshot of result
                screenshot = self.take_screenshot("demo_menu_click.png")
                results["screenshots"].append(screenshot)
                
            except Exception as e:
                results["errors"].append(f"Menu interaction failed: {str(e)}")
            
            # Get console logs
            results["console_logs"] = self.get_console_logs()
            
            # Check for JavaScript errors
            js_errors = [log for log in results["console_logs"] if log.get('level') == 'SEVERE']
            if js_errors:
                results["errors"].extend([log['message'] for log in js_errors])
            
            results["status"] = "success" if not results["errors"] else "failed"
            
        except Exception as e:
            results["status"] = "failed"
            results["errors"].append(f"Test failed: {str(e)}")
        
        return results
    
    def close(self):
        """Close browser"""
        if self.driver:
            self.driver.quit()
        if self.playwright:
            self.playwright.stop()


def test_local_demo():
    """Test the local cyberpunk demo"""
    tester = BrowserTester(headless=False)  # Show browser for debugging
    
    try:
        tester.start(engine="playwright")  # Use Playwright if available
        
        # Test local file
        demo_path = Path(__file__).parent.parent / "docs" / "index.html"
        demo_url = f"file://{demo_path.absolute()}"
        
        print(f"Testing demo at: {demo_url}")
        results = tester.test_cyberpunk_demo(demo_url)
        
        print(f"\nTest Results:")
        print(f"Status: {results['status']}")
        print(f"Themes tested: {results['themes_tested']}")
        print(f"Screenshots: {results['screenshots']}")
        
        if results['errors']:
            print(f"\nErrors found:")
            for error in results['errors']:
                print(f"  - {error}")
        
        return results
        
    except Exception as e:
        print(f"Test failed: {e}")
        return None
        
    finally:
        tester.close()


def test_github_pages():
    """Test the GitHub Pages demo"""
    tester = BrowserTester(headless=False)
    
    try:
        tester.start(engine="playwright")
        
        demo_url = "https://cambriantech.github.io/cyberpunk-cli/"
        print(f"Testing GitHub Pages demo at: {demo_url}")
        
        results = tester.test_cyberpunk_demo(demo_url)
        
        print(f"\nGitHub Pages Test Results:")
        print(f"Status: {results['status']}")
        print(f"Themes tested: {results['themes_tested']}")
        print(f"Screenshots: {results['screenshots']}")
        
        if results['errors']:
            print(f"\nErrors found:")
            for error in results['errors']:
                print(f"  - {error}")
        
        return results
        
    except Exception as e:
        print(f"GitHub Pages test failed: {e}")
        return None
        
    finally:
        tester.close()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test cyberpunk-cli web demos")
    parser.add_argument("--local", action="store_true", help="Test local demo")
    parser.add_argument("--github", action="store_true", help="Test GitHub Pages demo")
    parser.add_argument("--headless", action="store_true", help="Run in headless mode")
    parser.add_argument("--browser", default="chrome", help="Browser to use (chrome, firefox, safari)")
    
    args = parser.parse_args()
    
    if not args.local and not args.github:
        print("Please specify --local or --github")
        sys.exit(1)
    
    if args.local:
        test_local_demo()
    
    if args.github:
        test_github_pages()