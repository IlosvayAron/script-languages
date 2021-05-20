#!/usr/bin/env python3

def main():
    d = dict()
    for i in range(1,601):
        d[i]=0
    for i in range(601):
        lst = list(d.keys())
        for l in lst[i::i+1]:
            if d[l] == 0:
                d[l] = 1
            else:
                d[l] = 0
    print("Kegyelmet kap:", end=" ")
    for k in d.keys():
        if d[k] == 1:
            print(k, end=" ")
    print()
    
##############################################################################

if __name__ == "__main__":
    main()
