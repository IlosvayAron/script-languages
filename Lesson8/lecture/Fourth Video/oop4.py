#!/usr/bin/env python3

class Proba:
    i = 12345 # osztály változó, osztályhoz tartozik, nem a példányokhoz

    def hello(self):
        print("hello")

def main():
    print(Proba.i)
    
    p = Proba()
    p.hello()

##############################################################################

if __name__ == "__main__":
    main()