#!/usr/bin/env python3
from miller_rabin import is_prime_mr

def test(number):
    count = True
    while count:
        if is_prime_mr(number) == True and str(number) == str(number)[::-1]:
            count = False
        else:
            number += 1
    return number

def main():
    print(f'31 -> {test(31)}')      # 101
    print(f'130 -> {test(130)}')    # 131
    print(f'131 -> {test(131)}')    # 131
    print(f'1977 -> {test(1977)}')  # 10301

##############################################################################

if __name__ == "__main__":
    main()