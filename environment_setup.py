
import sys
import platform


def display_environment_info():
    """Display Python and system environment information."""
    print("AI Laboratory - Environment Setup")
    print("-" * 35)
    print("Python Version:", sys.version)
    print("Python Executable:", sys.executable)
    print("Operating System:", platform.system())
    print("System Architecture:", platform.machine())


if __name__ == "__main__":
    display_environment_info()
