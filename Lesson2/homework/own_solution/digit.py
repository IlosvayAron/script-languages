#!/usr/bin/env python3


def numbers_of_digit(base, power):
    number = int(base) ** int(power)
    str_number = str(number)
    length = len(str_number)
    return length
    
def exponentiation(base, power):
    number = int(base) ** int(power)
    return number


def main():
    print("Ez egy hatványozási feladat!")
    base = input("Add meg az alapot: ")
    power = input("Add meg a hatványt: ")
    result = exponentiation(base, power)
    number = numbers_of_digit(base, power) 
    print("A hatványozás eredménye: {}".format(result))
    print("A számjegyek száma pedig: {}".format(number))
    
    
if __name__ == "__main__":
    main()
