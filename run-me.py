import subprocess
import sys

# List of required modules and their versions (if needed)
required_modules = [
    "Flask",
    "googletrans==4.0.0-rc1",
    "PyPDF2"
]

def install_packages():
    for module in required_modules:
        try:
            print(f"Installing: {module} ...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(f"✅ {module} installed successfully.\n")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {module}. Please install it manually.")

if __name__ == "__main__":
    install_packages()
