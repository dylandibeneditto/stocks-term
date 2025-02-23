import sys
import tty
import termios

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)

        if key == "\x1b":
            key += sys.stdin.read(2)
            if key == "\x1b[A":
                key = "up"
            elif key == "\x1b[B":
                key = "down"
            elif key == "\x1b[C":
                key = "right"
            elif key == "\x1b[D":
                key = "left"
        return key
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
