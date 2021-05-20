#!/usr/bin/env python3
import sys

def cat(fname):
    try:
        f = open(fname)

        print("---", fname, "---")
        for line in f:
            print(line, end="")

        f.close()
    except:
        print("I/O error:", fname)


def main():
    args = sys.argv[1:]
    for fname in args:
        cat(fname)

##############################################################################

if __name__ == "__main__":
    main()