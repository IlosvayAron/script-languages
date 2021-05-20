#!/usr/bin/env python3
import sys
import random as r

UPTO = 100


def main():
    num = 1
    for i in range(UPTO):
        if num == 10:
            print(r.randint(0, 9), end="\n",)
            num = 1
        else:
            print(r.randint(0, 9), end="")
            num += 1
    print()


if __name__ == "__main__":
    main()