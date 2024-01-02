import subprocess
import sys, os

# Function to activate the virtual environment
def activate_virtualenv():
    venv_path = ".venv"  # Replace with your virtual environment path
    if sys.platform == "win32":
        activate_path = os.path.join(".\\", venv_path, "Scripts", "activate")
        print(f"path is: {activate_path}\n")
    else:
        activate_path = os.path.join(venv_path, "bin", "activate")

    activate_command = f" {activate_path}" if sys.platform != "win32" else activate_path
    subprocess.run(activate_command, shell=True)

def main():
    
    # Activate the virtual environment
    activate_virtualenv()

    # Run main.py within the virtual environment
    subprocess.run(["python", "main.py"])

if __name__ == '__main__':
    main()
