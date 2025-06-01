#!/usr/bin/env python3
"""
Setup script for cyberpunk-cli package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cyberpunk-cli",
    version="1.0.0",
    author="CambrianTech",
    author_email="contact@cambriantech.com",
    description="Cyberpunk-themed terminal menu system with multiple retro themes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CambrianTech/cyberpunk-cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Terminals",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=[
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.910",
        ],
    },
    keywords=[
        "terminal", "menu", "cyberpunk", "retro", "fallout", "matrix", "tron",
        "cli", "interface", "themes", "ascii", "terminal-ui", "console", "ui"
    ],
    entry_points={
        "console_scripts": [
            "cyberpunk-demo=cyberpunk_cli.examples.demo:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)