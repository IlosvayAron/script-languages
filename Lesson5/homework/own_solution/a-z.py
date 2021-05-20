#!/usr/bin/env python3
import os.path

# Nem jó megoldás
def alphabet():
    if os.path.islink('z-a.py'):
        letters = [chr(n) for n in range(122,97-1)]
        result = "".join(letters)
        print(f"{result}")
    else:
        letters = [chr(n) for n in range(97,122+1)]
        result = "".join(letters)
        print(f"{result}")


def main():
    alphabet()

##############################################################################

if __name__ == "__main__":
    main()