#!/usr/bin/env python3

def sum_of_digits(base: int, power: int) -> None:
    number = base ** power
    digits = number
    summ = 0
    while digits != 0:
       digit = digits % 10
       summ += digit
       digits //= 10 
    print(f"Alap: {base}, Hatvány: {power}")
    print(f"A hatványra emelés eredménye: {number}")
    print(f"Az eredmény számjegyeinek összege: {summ}")


def main() -> None:
    sum_of_digits(2,15)
    print("-" * 50)
    sum_of_digits(2,1000)

##############################################################################

if __name__ == "__main__":
    main()
