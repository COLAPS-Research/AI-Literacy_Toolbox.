import sys
import subprocess

MINIMUM_PYTHON_VERSION = (3, 11)


def check_python_version() -> bool:
    """
    Checks python version to make sure it is compatible with required packages.
    :return:
    """
    if sys.version_info < MINIMUM_PYTHON_VERSION:
        return False
    return True


def main():
    """
    Checks platform to call script that fits the needs to create a venv.
    :return:
    """
    python_installed = check_python_version()

    if not python_installed:
        sys.exit(
            "This application requires Python 3.11 or higher. Please upgrade your Python version."
        )
    # Determine the platform and run the corresponding setup script
    platform = sys.platform
    if platform.startswith("linux") or platform == "darwin":
        subprocess.call(["chmod", "+x", "../scripts/setup_mac_linux.sh"])
        subprocess.call(["sh", "../scripts/setup_mac_linux.sh"])
    elif platform == "win32":
        git_bash_path = r"C:\Program Files\Git\bin\bash.exe"
        subprocess.call([git_bash_path, "../scripts/setup_windows.sh"])
    else:
        sys.exit(f"Unsupported platform: {platform}")


if __name__ == "__main__":
    main()
