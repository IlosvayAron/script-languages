#!/usr/bin/env python3
import sys

NUMBERS = "0123456789"

def double_digits(text: str) -> str:
    res = []
    for t in text:
        for n in NUMBERS:
            if t == n:
                for i in range(1):
                    res.append(t)
        res.append(t)
        result = "".join(res)
    return result



def main() -> None:
    if len(sys.argv) != 2:
        print("Hibás paraméterezés! Egyetlen sztringet kell megadni!")
    else:
        print(double_digits(sys.argv[1]))

##############################################################################

if __name__ == "__main__":
    main()