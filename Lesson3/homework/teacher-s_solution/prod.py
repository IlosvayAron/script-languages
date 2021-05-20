#!/usr/bin/env python3
"""
Írjunk függvényt, mely kap egy egészeket tartalmazó listát
s visszaadja a listában lévő elemek szorzatát.

Definíció szerint egy üres lista elemeinek a szorzata 1.
"""


def product(numbers):
    p = 1
    for x in numbers:
        p *= x
    #
    return p 


def main():
    numbers = [1, 2, 3, 4, 5]
    print(f"Lista elemeinek szorzata: {numbers} -> {product(numbers)}")    # 120
    print("Üres lista elemeinek szorzata: [] ->", product([]))         # 1

##############################################################################

if __name__ == "__main__":
    main()