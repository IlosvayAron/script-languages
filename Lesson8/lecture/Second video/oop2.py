#!/usr/bin/env python3


class Bag:
    def __init__(self):
        self.data = []

    def add(self, number):
        self.data.append(number)

    def add_twice(self, number):
        # 1. módszer - konzisztens problémák merülhetnek fel(nem egységes/nem elentmondásoktól mentes)
        #self.data.append(number)
        #self.data.append(number)
        # 2. módszer - egyben szebb is
        self.add(number)
        self.add(number)

    def __str__(self):
        return "Bag({repr})".format(repr = str(self.data)) # Bag objektum


def main():
    b = Bag()
    b.add(5)
    print(b)
    b.add(3)
    print(b)
    b.add_twice(9)
    print(b)

##############################################################################

if __name__ == "__main__":
    main()