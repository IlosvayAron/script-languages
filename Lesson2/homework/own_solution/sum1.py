#!/usr/bin/env python3


import sys


#A) Számok bekérése parancssori argumentumként!       
def main():
    if len(sys.argv) < 3:
        print('Nem adtad meg a második számot!')
    else:
        sum = int(sys.argv[1]) + int(sys.argv[2])
        print('A két szám összege: {0}'.format(sum))
    
    
if __name__ == "__main__":
    main()
