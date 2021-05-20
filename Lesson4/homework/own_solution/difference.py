#!/usr/bin/env python3


def square_of_sum_of_numbers():
    number = sum(range(1, 100+1)) ** 2
    return number


def sum_of_squares():
    number = 0
    for i in range(1, 100+1):
        number += (i ** 2)
    return number


def main():
    num1 = square_of_sum_of_numbers()
    num2 = sum_of_squares()
    print( "\nI. Az első száz természetes szám összegének a négyzete: {n1}".format(n1=num1))
    print( "II. Az első száz természetes szám négyzetösszege: {n2}".format(n2=num2))
    result = num1 - num2
    print("Az I. és II. közötti külömbség: {0} - {1} = {2}\n".format(num1,num2,result))

##############################################################################

if __name__ == "__main__":
    main()