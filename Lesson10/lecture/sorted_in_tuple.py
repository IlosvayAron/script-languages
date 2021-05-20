#!/usr/bin/env python3

"""
    Rendezzük a rekordokat az utolsó oszlop értéke szerint.
"""

def my_func1(t):
    return t[-1]

def main():
    data = [ 
        (1,'Albany','NY',162692),
        (3,'Allegany','NY',11986),
        (121,'Wyoming','NY',8722),
        (123,'Yates','NY',5094)
    ]
    print(data)
    print(sorted(data, key=my_func1))
    # Anonim függvény megadása! Csak olyan fv. megengedett, aminek a törzse egyetlen egy kifejezés.
    print("-" * 40, "Anonim fv használata", "-" * 40)
    print(sorted(data, key=lambda t: t[-1]))

##############################################################################

if __name__ == "__main__":
    main()