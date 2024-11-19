import json
import requests
import os
import subprocess
import webbrowser
import sys

# Constants
DB_URL = "https://sctech.netlify.app/scpkg_db.json"
DB_FILE = "scpkg_db.json"
INSTALLED_FILE = "installed_packages.json"
VERSION = "1.0.0"  # Version of scpkg

# Initialize the installed packages file if it doesn't exist
if not os.path.exists(INSTALLED_FILE):
    with open(INSTALLED_FILE, "w") as file:
        json.dump({}, file)


def update_db():
    """Update the local database by fetching the latest JSON from the remote URL."""
    response = requests.get(DB_URL)
    if response.status_code == 200:
        with open(DB_FILE, "w") as db_file:
            db_file.write(response.text)
        print("Database updated successfully.")
    else:
        print("Failed to update database.")


def load_db():
    """Load the local JSON database."""
    with open(DB_FILE, "r") as db_file:
        return json.load(db_file)


def load_installed():
    """Load the list of installed packages."""
    with open(INSTALLED_FILE, "r") as file:
        return json.load(file)


def save_installed(installed):
    """Save the installed packages data."""
    with open(INSTALLED_FILE, "w") as file:
        json.dump(installed, file, indent=4)


def confirm_action(auto_confirm=False):
    """Prompt the user to confirm an action unless auto-confirm is enabled."""
    if auto_confirm:
        return True
    choice = input("Do you want to continue? (y/n): ").strip().lower()
    return choice == 'y'


def list_packages():
    """List all available packages."""
    db = load_db()
    print("Available packages:")
    for pkg in db:
        print(f"- {pkg['name']}: {pkg['desc']} (v{pkg['version']})")


def search_package(name):
    """Search for a specific package by name."""
    db = load_db()
    for pkg in db:
        if name.lower() in pkg['name'].lower():
            print(f"Found package: {pkg['name']} - {pkg['desc']} (v{pkg['version']})")
            return
    print("Package not found.")


def install_package(name, auto_confirm=False):
    """Install a package by executing its installation command."""
    db = load_db()
    installed = load_installed()

    for pkg in db:
        if pkg['name'] == name:
            if name in installed:
                print(f"{name} is already installed.")
            else:
                print(f"Installing {name} - {pkg['desc']} (v{pkg['version']})")
                if confirm_action(auto_confirm):
                    subprocess.run(pkg["install"], shell=True)
                    installed[name] = pkg
                    save_installed(installed)
                    print(f"{name} installed successfully.")
            return
    print("Package not found.")


def remove_package(name, auto_confirm=False):
    """Remove a package by executing its removal command."""
    installed = load_installed()
    if name in installed:
        print(f"Removing {name}...")
        if confirm_action(auto_confirm):
            subprocess.run(installed[name]["remove"], shell=True)
            del installed[name]
            save_installed(installed)
            print(f"{name} removed successfully.")
    else:
        print("Package not installed.")


def update_package(name, auto_confirm=False):
    """Update a specific package by executing its update command."""
    installed = load_installed()
    if name in installed:
        print(f"Updating {name}...")
        if confirm_action(auto_confirm):
            subprocess.run(installed[name]["update"], shell=True)
            print(f"{name} updated successfully.")
    else:
        print("Package not installed.")


def upgrade_all(auto_confirm=False):
    """Upgrade all installed packages."""
    installed = load_installed()
    for name, pkg in installed.items():
        print(f"Upgrading {name}...")
        if confirm_action(auto_confirm):
            subprocess.run(pkg["update"], shell=True)
            print(f"{name} upgraded to latest version.")


def show_help():
    """Display help information for scpkg."""
    help_text = """
    scpkg - sctech's package manager

    Commands:
      update-db               Update the local package database
      list                    List all available packages
      search <name>           Search for a package by name
      install <name>          Install a package
      remove <name>           Remove a package
      update <name>           Update a specific package
      upgrade                 Upgrade all installed packages
      src <name>              Open the GitHub repo for a package

    Flags:
      -h                      Show this help message
      -v                      Display version of scpkg
      -y                      Automatically confirm prompts
    """
    print(help_text)


def open_source(name):
    """Open the GitHub repository URL for the specified package."""
    db = load_db()
    for pkg in db:
        if pkg['name'] == name:
            webbrowser.open(pkg['src'])
            print(f"Opening source for {name}: {pkg['src']}")
            return
    print("Package not found.")


def main():
    auto_confirm = '-y' in sys.argv
    if '-h' in sys.argv:
        show_help()
        return
    if '-v' in sys.argv:
        print(f"scpkg version {VERSION}")
        return

    # Filter out flags for easier command parsing
    args = [arg for arg in sys.argv[1:] if arg not in ['-y', '-h', '-v']]
    if len(args) < 1:
        print("Usage: scpkg <command> [package_name]")
        return

    command = args[0]
    if command == "update-db":
        update_db()
    elif command == "list":
        list_packages()
    elif command == "search" and len(args) > 1:
        search_package(args[1])
    elif command == "install" and len(args) > 1:
        install_package(args[1], auto_confirm)
    elif command == "remove" and len(args) > 1:
        remove_package(args[1], auto_confirm)
    elif command == "update" and len(args) > 1:
        update_package(args[1], auto_confirm)
    elif command == "upgrade":
        upgrade_all(auto_confirm)
    elif command == "src" and len(args) > 1:
        open_source(args[1])
    else:
        print("Unknown command or missing argument.")
        show_help()


if __name__ == "__main__":
    main()
