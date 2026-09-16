import os
import sys
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_and_install_requirements():
    required_packages = ['yt-dlp', 'colorama']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print("[!] Missing packages detected. Installing requirements...")
        for package in missing_packages:
            print(f"[+] Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("[✓] All requirements installed successfully!\n")

if __name__ == "__main__":
    clear_screen()
    check_and_install_requirements()
    
    try:
        import main
        main.main()
    except Exception as e:
        print(f"Error starting main application: {e}")