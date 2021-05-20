#!/usr/bin/env python3

def diamond(number):
    number = int(number)
    if number % 2 == 0:
        print("Csak páratlan számot lehet megadni magasságnak!")
    else:
        for i in range(-number + 1, number + 1, 2):
            print(((number - abs(i)) * '*').center(number))


def main():
    num = input("Gyémánt magasságát: ")
    diamond(num)

##############################################################################

if __name__ == "__main__":
    main()