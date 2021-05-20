#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) == 4:
        lst1 = []
        del sys.argv[0]
        for line in sys.argv:
            lst1.append(len(line))
        leghosszabb = max(lst1)
        lst2 = []
        for arg in sys.argv:
            lst2.append(arg)
        lst3 = []
        for line in lst2:
            while len(line) != leghosszabb:
                line = line + 'X'
            lst3.append(line)
        i = 0
        szamlalo = 0
        result = ""
        while i < leghosszabb:
            for l in lst3:
                result += l[szamlalo]
            szamlalo += 1
            i += 1
        print(result)
    else:
        print("Hiba! Adj meg pontosan három szringet!")

##############################################################################

if __name__ == "__main__":
    main()