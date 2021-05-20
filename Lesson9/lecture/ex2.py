#!/usr/bin/env python3

"""
    ex2.py
"""

from pygyak import is_prime # így nem kell átnevezni hanem használhatom egyszerűen az 'is_prime()' fv.-t


def main():
    primes = [i for i in range(200) if is_prime(i)]
    print(sum(primes))

##############################################################################

if __name__ == "__main__":
    main()