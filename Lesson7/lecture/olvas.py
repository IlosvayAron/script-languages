#!/usr/bin/env python3

def main():
    f = open("szoveg.txt", 'r')
    for line in f:
        print(line.rstrip('\n'))
    f.close()


##############################################################################

if __name__ == "__main__":
    main()