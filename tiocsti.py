import argparse
import fcntl
import os
import termios

def push(s):
    fd = 0
    for fd in range(0, 3):
        try:
            fcntl.ioctl(fd, termios.TIOCSTI, s[0])
        except IOError:
            continue
        else:
            break
    else:
        fd = os.open('/dev/tty', os.O_RDONLY)
        fcntl.ioctl(fd, termios.TIOCSTI, s[0])
    for ch in s[1:]:
        fcntl.ioctl(fd, termios.TIOCSTI, ch)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('command', metavar='COMMAND')
    ap.add_argument('rest', nargs='*', help=argparse.SUPPRESS)
    options = ap.parse_args()
    cmdline = ' '.join([options.command] + options.rest)
    push(' {cmd}\n'.format(cmd=cmdline))

if __name__ == '__main__':
    main()
