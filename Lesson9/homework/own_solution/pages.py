#!/usr/bin/env python3

def printable_pages(pages: list) -> list:
    lst = pages.split(',')
    res = []
    for num in lst:
        if '-' not in num:
            res.append(int(num))
        else:
            interval = num.split('-')
            lower = interval[0]
            upper = interval[-1]
            for i in range(int(lower), int(upper)+1):
                res.append(i) 
    return res

def main():
    print("Minta az inputra: 1-4,7,9,11-15")
    text = input('Add meg a nyomtatandó oldalakat: ')
    print("Nyomtatandó oldalak:", printable_pages(text))

##############################################################################

if __name__ == "__main__":
    main()