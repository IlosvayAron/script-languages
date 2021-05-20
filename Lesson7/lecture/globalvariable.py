#!/usr/bin/env python3

PI = 3.14159 # konstans

counter = 0


def f2():
    # módosítja a globális counter változó értékét
    global counter
    counter = 42


def f1():
    # a 'counter' egy lokális változó lesz -> nem módosítja a globális értéket
    counter = 5
    print('f1:', counter)


def f0():
    # a globális 'counter' változóra hivatkozik 
    print('f0:', counter)


def main():
    # minden esetben a viselkedás a következő: ellenőrzi, hogy lokális-e a változó
    # ha nem akkor globálisan keresi és azzal dolgozik
    print('PI:', PI)
    f1()
    f0()
    f2()
    print('main:', counter)

##############################################################################

if __name__ == "__main__":
    main()