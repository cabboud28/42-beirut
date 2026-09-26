import os
# we use import os to get the path of the virtual environment and site-packages directory
import sys
# we use import sys to get the current Python executable and version information and to check if we're in a virtual environment or not


def main() -> None:
    print("MATRIX STATUS: ", end="")

    if sys.prefix != sys.base_prefix:
        # we use sys.prefix to get the path of the current virtual environment and sys.base_prefix to get the path of the base Python installation
        py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        # we use sys.version_info to get the current Python version and format it as a string (difference between major and minor is that major is the first number in the version and minor is the second number)
        site_packages = os.path.join(
            sys.prefix, "lib", f"python{py_version}", "site-packages"
        )
        # we use os.path.join to construct the path to the site-packages directory of the current virtual environment (difference between lib and site-packages is that lib is the directory where Python libraries are stored and site-packages is the directory where third-party packages are installed)
        print("Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print(
            "Safe to install packages without affecting\nthe global system.\n"
        )
        print(f"Package installation path:\n{site_packages}")
    else:
        print("You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
