#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    Sztringget add vissza.

    Visszatér a függvénynek első paraméterként átadott sztring
    azon karaktereivel, melyek a második paraméterben megadott
    sztringben benne vannak.
    """
    result = ""
    for t in text:
        if t in chars:
            result += t   
    print('valid("{t}", "{c}")'.format(t=text, c=chars), end=" -> ")
    print('"{r}"'.format(r=result))


def main():
    valid("Barking!")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")

##############################################################################

if __name__ == "__main__":
    main()