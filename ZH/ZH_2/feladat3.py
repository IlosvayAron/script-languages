#!/usr/bin/env python3

def main():
    f = open('numbers.csv')
    lines = f.read().splitlines()
    f.close()
    en = 0
    hu = 0
    angol_ossz = []
    magyar_ossz = []
    for ln in lines:
        res = ln.split(';')
        for r in res:
            if r != res[-1] and "." in r:
                en += 1
                angol_ossz.append(r)
            elif r != res[-1] and "," in r:
                hu += 1
                magyar_ossz.append(r)
    angol_res = 0
    magyar_res = 0
    for a in angol_ossz:
        angol_res += float(a)
    for m in magyar_ossz:
        m = m.replace(",",".")
        magyar_res += float(m)
    print(f"A fájlban {en} db angol és {hu} db magyar szám található!")
    print(f"Angol számok összege: {angol_res}")
    print(f"Magyar számok összege: {magyar_res}")

##############################################################################

if __name__ == "__main__":
    main()