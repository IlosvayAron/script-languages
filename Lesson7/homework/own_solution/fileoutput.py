#!/usr/bin/env python3
# coding: utf-8

def main():
    input = open("string1.py", "r")
    output = open("string1_clean.py", "w")
    for line in input:
        if not line.startswith('#') and '#' not in line:
            line = line.rstrip('\n')
            print(line, file=output)
    input.close()
    output.close()

##############################################################################

if __name__ == "__main__":
    main()