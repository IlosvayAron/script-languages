#!/usr/bin/env python3


def reverse_number(number):
    revnumber = number[::-1]
    return int(revnumber)
    

def main():
    s = input("Adj meg egy számot: ")
    number = reverse_number(s) 
    print("{0} -> {1}".format(s, number))
    
    
if __name__ == "__main__":
    main()
