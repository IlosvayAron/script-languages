#!/usr/bin/env python3

def rek_palindrom(s):
    if len(s) < 1:
        return s
    else:
        if s[0] == s[-1]:
            return rek_palindrom(s[1:-1])
        else:
            s = "X" * len(s)
            return s

def main():
    f = open("szoveg.txt")
    lines = f.read().splitlines()
    f.close()
    #print(lines)
    lst = []
    for ln in lines:
        ln = ln.split()
        lst.append(ln)
    #print(lst)
    res = []
    result = []
    for lt in lst:
        for l in lt:
            l = rek_palindrom(l)
            res.append(l)
        result.append(res)
    print(lst)

##############################################################################

if __name__ == "__main__":
    main()