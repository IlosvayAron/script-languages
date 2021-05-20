#!/usr/bin/env python3


def is_palindrom(s: str) -> bool:
    return s == s[::-1]


def main() -> None:
    print("Palindrom vagy sem?")
    s = input("Adj meg egy szót: ") 
    print(is_palindrom(s))
    
    
if __name__ == "__main__":
    main()
