#!/usr/bin/env python3

# Fv. és visszatérési érték annotáció 
def add(a: int, b: int) -> int:
    return a + b


def main():
    # Változó annotáció
    a: int = 6
    # a: str = 6 -> mypy hibát jelez 
    print(add(2, 4))
    #print(add("aa", "bb"))

##############################################################################

if __name__ == "__main__":
    main()
