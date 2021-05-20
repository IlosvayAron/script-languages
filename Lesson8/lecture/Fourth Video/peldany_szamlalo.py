#!/usr/bin/env python3

""" Írj programot ami megszémolja hányor példányosítottad az osztályt!"""

class Proba:
    cnt = 0

    # Mivel a konstruktor meghívódik minden példányosítás esetén ezért tökéletes a feladatra.
    def __init__(self):
        Proba.cnt += 1

def main():
    p1 = Proba()
    p2 = Proba()
    p3 = Proba()
    print("Példányok száma:", Proba.cnt)
    p4 = Proba()
    p5 = Proba()
    print("Példányok száma:", Proba.cnt)


##############################################################################

if __name__ == "__main__":
    main()