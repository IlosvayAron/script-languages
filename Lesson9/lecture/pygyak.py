#!/usr/bin/env python3
def is_prime(n):
    """
    Decide whether a number is prime or not.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True

def hello():
    return 'Hello world!'

if __name__ == "__main__":
    #for i in range(2,20):
    #    if is_prime(i):
    #        print(f"{i} prímszám")
    number = input("Adj meg egy számot: ")
    if is_prime(int(number)):
        print(f"{number} prímszám")
    else:
        print(f"{number} nem prímszám")