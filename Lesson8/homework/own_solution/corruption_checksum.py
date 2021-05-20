#!/usr/bin/env python3

def main():
    f = open("day02.txt", "r")
    lines = [line.rstrip("\n") for line in f.readlines()]
    res = []
    for l in lines:
        num = l.split()
        numbers = []
        for n in num:
            numbers.append(int(n))
        diff = max(numbers) - min(numbers)
        res.append(diff)
    print(f"Az input táblázatunk ellenőrző összege: {sum(res)}")
    f.close()

##############################################################################

if __name__ == "__main__":
    main()