#!/usr/bin/env python3


def munchausen_numbers(limit):
    """
    Ez a függvény megkeresi az összes Munchausen számot a praméterében megadott értékig.
    """
    result = []
    for n in range(limit):
        summ=0
        for i in str(n):
            if int(i) == 0:
                summ += 0
                if summ == n:
                    result.append(summ)
            else:
                summ += int(i) ** int(i)
                if summ == n:
                    result.append(summ)
    return result


def main():
    task1 = munchausen_numbers(10000)
    #task2 = munchausen_numbers(440000000)
    print("Munchausen számok 10000-ig: {t}".format(t=task1))

##############################################################################

if __name__ == "__main__":
    main()