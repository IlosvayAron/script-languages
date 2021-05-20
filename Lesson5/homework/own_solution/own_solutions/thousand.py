#!/usr/bin/env python3


def summ():
    """
    Visszaadja az 1000-nél kisebb számok összegét, melyek 3-nak vagy 5-nek a többszörösei.
    """
    numbers = [n for n in range(1,1000) if n % 3 == 0 or n % 5 == 0]
    result = sum(numbers)
    print(f"Lista: {numbers}")
    print(f"\n1000-nél kisebb számok összege, melyek 3-nak vagy 5-nek a többszörösei: {result}")


def main():
    summ()

##############################################################################

if __name__ == "__main__":
    main()