#!/usr/bin/env python3
from random import randint

def main():
    lotteryNumbers = []
    for i in range(6):
        number = randint(1,45)
        while number in lotteryNumbers:
            number = randint(1,45)
        lotteryNumbers.append(number)
    print(f"Nyerőszámok: {lotteryNumbers} {sum(lotteryNumbers)}")

##############################################################################

if __name__ == "__main__":
    main()