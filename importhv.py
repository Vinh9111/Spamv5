import subprocess

def install_packages(packages):
    for package in packages:
        try:
            subprocess.check_call(["pip", "install", package, "--quiet"])
            print(f"")
        except subprocess.CalledProcessError as e:
            print(f"")
packages = ["colorama", "alive-progress", "requests"]
install_packages(packages)
