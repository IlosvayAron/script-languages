#!/usr/bin/env python3

def xor(str1, str2):
    if str1 == 'None':
        str1 = None
    elif str2 == 'None':
        str2 = None

    first = bool(str1)
    second = bool(str2)
    if first == True and second == False:
        print("\nTeljesül a feltétel miszerint az egyik érték 'Igaz' a másik 'Hamis' ")
        print("Első input kiértékelve: {f}".format(f=first))
        print("Második input kiértékelve: {s}".format(s=second))
    elif first == False and second == True:
        print("\nTeljesül a feltétel miszerint az egyik érték 'Igaz' a másik 'Hamis' ")
        print("Első input kiértékelve: {f}".format(f=first))
        print("Második input kiértékelve: {s}".format(s=second))
    else:
        print("\nNem teljesül a feltétel miszerint az egyik érték 'Igaz' a másik 'Hamis' ")
        print("Első input kiértékelve: {f}".format(f=first))
        print("Második input kiértékelve: {s}".format(s=second))


def main():
    print("Adj meg két értéket!")
    str1 = input("Első változó értéke: ")
    str2 = input("Második változó értéke: ")
    xor(str1,str2)

##############################################################################

if __name__ == "__main__":
    main()