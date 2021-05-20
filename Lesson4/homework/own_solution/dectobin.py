#!/usr/bin/env python3

def dectobin(number):
    number = int(number)
    res = []
    while number // 2 != 0:
        remainder = number % 2
        number = number // 2
        res.append(str(remainder))
    res.append(str(number))
    return "".join(res[::-1])


def main():
    print("Adj meg egy számot!")
    number = input("Szám: ")
    print("A szám bináris alakja:", dectobin(number))

##############################################################################

if __name__ == "__main__":
    main()