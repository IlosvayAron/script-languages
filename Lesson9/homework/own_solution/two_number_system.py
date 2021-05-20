#!/usr/bin/env python3
import counting_helper as ch

def two_palindrom(limit: int) -> int:
    res = []
    for n in range(1, limit):
        if ch.is_palindrom(n) and ch.is_palindrom(ch.dectobin(n)):
            res.append(n)
    return sum(res)

def main():
    print('\nOlyan számokat adtunk össze, melyek 10-es és 2-es számrendszerben is palindromok!')
    print('1 milliónál kisebb pozítiv számok összege:', two_palindrom(1_000_000))
    

##############################################################################

if __name__ == "__main__":
    main()