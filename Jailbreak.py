#!/usr/bin/env python3
"""
The challenge is easy!
Just exit this annoying code!
Easy right?
"""
import signal
from sys import exit as bye

def why():
    bye(0)

def hmmm(sig,frame):
    if sig == 8:
        handler(sig,frame)
    else:
        print("\nLOL NOOB", end="")



def handler(signal_received, frame):
    bye(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, hmmm)
    signal.signal(signal.SIGTSTP, hmmm)
    signal.signal(signal.SIGQUIT, signal.SIG_IGN)
    signal.signal(signal.SIGFPE, hmmm)
    while True:
        try:
            var = input("Signal(Madness)>> ")
            print(ord(var[-2]) // (ord(var[-15]) >> 1))
        except(EOFError, IndexError):
            print(end="\r")
            print(end='\x1b[2K')
            continue
        except ZeroDivisionError:
            why()
        except Exception:
            continue
