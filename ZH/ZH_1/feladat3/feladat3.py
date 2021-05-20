#!/usr/bin/env python3

def main():
    f = open("input.txt", "r")
    #lines = [line.rstrip('\n') for line in f.readlines()]
    text = f.read().rstrip('\n')
    f.close()
    
##############################################################################

if __name__ == "__main__":
    main()