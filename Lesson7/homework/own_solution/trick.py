#!/usr/bin/env python3

NUMBERS = """
01111001 01101111
01110101 01110100
01110101 00101110
01100010 01100101
00101111 01100100
01010001 01110111
00110100 01110111
00111001 01010111
00111001 01010111
01100111 01011000
01100011 01010001
"""

def main():
    d = dict()
    lst = NUMBERS.split()
    res = []
    res2 = []
    for l in lst:
        num = int(l)
        sum = 0
        i = 0
        while num != 0:
            rem = num % 10
            sum = sum + rem * pow(2,i)
            num = num // 10
            i += 1
        res.append(sum)
    print("Megfejtés: ", end=' ')
    for r in res:
        print(chr(r), end='')
    print()
        

##############################################################################

if __name__ == "__main__":
    main()
