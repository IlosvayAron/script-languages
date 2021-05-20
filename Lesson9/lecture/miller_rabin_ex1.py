#!/usr/bin/env python3

"""
    mr_ex2.py
"""

from miller_rabin import is_prime_mr


def main():
    primes = [i for i in range(100) if is_prime_mr(i)]
    print(primes)

##############################################################################

if __name__ == "__main__":
    main()