#!/usr/bin/env python3

import sys


# Ha Batman az első paraméter a parancssorban akkor írd ki "Denevérveszély!"
# akkor is ha Robin a név, különben pedig az első paramétert  


def hello(s):
    if s == "Batman" or s == "Robin":
        print("Denevérveszély!")
    else:
        print("Hello " + s + "!")


def main():
    name = sys.argv[1]
    hello(name)
    
if __name__ == "__main__":
    main()
