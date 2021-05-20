#!/usr/bin/env python3

def main():
    f = open("input.txt", "r")
    for line in f:
        line = line.rstrip("\n")
        print(line)
    f.close()
    
##############################################################################

if __name__ == "__main__":
    main()