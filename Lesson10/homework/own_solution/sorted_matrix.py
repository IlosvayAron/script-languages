#!/usr/bin/env python3
"""
    Tekintsük a köv. mátrixot:

    li=[ [2,6],[1,3],[5,4] ]

    Rendezzük a mátrix sorait a 2. oszlop szerint:

    [ [1, 3], [5, 4], [2, 6] ]
"""

def sort_by_column(lst):
    return lst[-1]


def main():
    li=[ [2,6],[1,3],[5,4] ]
    print("Eredeti lista: ", li)
    print("-"*10, "Rendezett lista", "-"*10)
    print("Deklarált függvény:", sorted(li, key=sort_by_column))
    print("Anonim függvény:", sorted(li, key=lambda c: c[-1]))

##############################################################################

if __name__ == "__main__":
    main()