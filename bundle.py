"""
@0x360x36

this script is used to install base apps on macOS
it will install the following apps:
- brew
- oh-my-zsh
- iterm2
"""

import os
import subprocess

# brew
def install_brew():
    """
    install brew
    """
    # check if brew is installed
    if os.path.exists("/opt/homebrew/bin/brew"):
        print("brew is already installed")
        return

    # install brew
    print("installing brew...")
    try:
        subprocess.run(
            ["/bin/bash", "-c", "curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh | bash"],
            check=True
        )
        print("brew installed")
    except subprocess.CalledProcessError:
        print("Failed to install brew")

# oh-my-zsh
def install_oh_my_zsh():
    """
    install oh-my-zsh
    """
    # check if oh-my-zsh is installed
    if os.path.exists(os.path.expanduser("~/.oh-my-zsh")):
        print("oh-my-zsh is already installed")
        return

    # install oh-my-zsh
    print("installing oh-my-zsh...")
    try:
        subprocess.run(
            ["sh", "-c", "curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sh"],
            check=True
        )
        print("oh-my-zsh installed")
    except subprocess.CalledProcessError:
        print("Failed to install oh-my-zsh")

# iterm2
def install_iterm2():
    """
    install iterm2
    """
    # check if iterm2 is installed
    if os.path.exists("/Applications/iTerm.app"):
        print("iTerm2 is already installed")
        return

    # install iterm2
    print("installing iTerm2...")
    try:
        subprocess.run(
            ["brew", "install", "--cask", "iterm2"],
            check=True
        )
        print("iTerm2 installed")
    except subprocess.CalledProcessError:
        print("Failed to install iTerm2")

# main
def main():
    """
    main execution
    """
    print(
        """
        this script is used to install base apps on macOS
        it will install the following apps:
        - oh-my-zsh
        - iterm2
        - brew
        """
    )
    install_brew()
    install_oh_my_zsh()
    install_iterm2()

if __name__ == "__main__":
    main()