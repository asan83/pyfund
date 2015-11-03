"""keypress - A module for detecting a single keypress."""

try:
    import msvcrt

    def getkey():
        """Wait for a keypress and return a single character string."""
        print("We are on Windows")
        return msvcrt.getch()

except ImportError:
    import sys
    import tty
    import termios

    def getkey():
        """Wait for a keypress and return a single character string."""
        print("We are on Linux or MacOS")
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch

# If either of the Unix-specifc tty or termios are not found,
# we allow ImportError to propagate from here.