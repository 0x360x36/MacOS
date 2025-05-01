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
    # Check if Homebrew is installed
    if not os.path.exists('/usr/local/bin/brew'):
        print("Homebrew is not installed. Please install it first.")
        return

    # List of tools to install
    tools = [
        'nmap'
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
