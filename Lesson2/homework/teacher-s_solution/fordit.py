#!/usr/bin/env python3
"""
Írjunk függvényt, mely kap egy pozitív egész számot,
s visszatérési értékként a szám fordítottját adja vissza mint egész számot.

Példa: 1977 → 7791; 12568 → 86521.
"""


def fordit(n):
    return int(str(n)[::-1])


def main():
    n = 1983
    print(f'Szám:', n)           # 1983
    print(f'Fordítottja:', fordit(n))   # 3891

##############################################################################

if __name__ == "__main__":
    main()