#!/usr/bin/env python3

"""
    ex2.py
"""

import pygyak as p


def main():
    # 1. solution
    #primes = [i for i in range(100) if is_prime(i)]
    #print(primes)
    # 2. solution
    for n in range(100):
        if p.is_prime(n):
            print(n, end=' ')
    print()

##############################################################################

if __name__ == "__main__":
    main()