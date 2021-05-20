#!/usr/bin/env python3
"""
A program interaktív módon kérje be a nevünket. A nevünk előtt és után hagyjunk szóközöket.
A program üdvözöljön minket a következő módon: Hello <input_nev>!
"""


def main():
    name = input("Neved: ")
    name = name.strip()
    print("Hello " + name + "!")

##############################################################################

if __name__ == "__main__":
    main()