"""
@0x360x36

using brew the following tools will be installed:
- nmap
"""

import os
import subprocess

def install_tools():
    """
    Install the required tools using Homebrew.
    """
    # List of tools to install
    tools = [
        'nmap',
        'nuclei'
    ]

    for tool in tools:
        print(f"Installing {tool}...")
        subprocess.run(['brew', 'install', tool], check=True)

def main():
    """
    Main function to install tools.
    """
    # Install the tools
    print("Installing tools...")
    install_tools()
    print("Tools installed successfully.")

if __name__ == "__main__":
    # Run the main function
    main()
