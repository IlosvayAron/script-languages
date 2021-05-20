#!/usr/bin/env python3
"""
Olvassunk be két számot s írjuk ki a két szám összegét.
"""
import sys

def main():
    if len(sys.argv) != 3:
        #print("You did not specify two command line arguments!")
        print("Nem kettő argumentumot adott meg!")
        exit(1) # kilépünk a programból és 1-es hibakódot ad0 vissza
    #else
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a + b)


##############################################################################

if __name__ == "__main__":
    main()