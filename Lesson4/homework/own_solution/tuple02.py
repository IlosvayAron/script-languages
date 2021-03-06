#!/usr/bin/env python3

import math


def distance(p1, p2):
    p3 = (6, 2) # A derékszög koordinátája a videóban lévő rajz alapján
    a = math.sqrt(((p3[0] - p1[0]) ** 2) + ((p3[1] - p1[1]) ** 2))
    b = math.sqrt(((p2[0] - p3[0]) ** 2) + ((p2[1] - p3[1]) ** 2))
    c = math.sqrt(a ** 2 + b ** 2)
    return c


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()
