#!/usr/bin/env python3

def sumofdigits(lst):
    res = [] 
    for element in lst: 
        summ = 0
        for digit in str(element): 
            summ += int(digit) 
        res.append(summ)
    return sum(res)


def main():
    summ = sum((range(1,100+1)))
    result = sumofdigits(range(1,100+1))
    print("A számok összege 1-től 100-ig:",summ)
    print("A számok számjegyeinek összege 1-től 100-ig:",result)

##############################################################################

if __name__ == "__main__":
    main()