#!/usr/bin/env python3
import random as rd

def shuffled(lst: list) -> list:
    result = []
    while len(result) != len(lst):
        num = rd.choice(lst)
        if num not in result:
            result.append(num)
    return result

def main():
    numbers = [3, 8, 2, 5, 9, 1, 7, 10, 4, 6]
    print('Eredeti lista:', numbers)
    mixed_numbers = shuffled(numbers)
    print('-' * 45)
    print('Kevert lista:', mixed_numbers)
    print('Eredeti lista:', numbers)
    print('-' * 45)
    print('Kevert lista utolsó eleme:', mixed_numbers[-1])


##############################################################################

if __name__ == "__main__":
    main()