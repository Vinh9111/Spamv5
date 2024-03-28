import subprocess

def install_packages(packages):
    for package in packages:
        try:
            subprocess.check_call(["pip", "install", package, "--quiet"])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}: {e}")
packages = ["colorama", "alive-progress", "requests"]
install_packages(packages)
