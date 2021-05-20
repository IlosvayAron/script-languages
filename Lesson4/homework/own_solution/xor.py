#!/usr/bin/env python3

def xor(str1, str2):
    first = bool(str1)
    second = bool(str2)
    if first == True and second == False:
        print("Teljesül a feltétel miszerint az egyik érték 'Igaz' a másik 'Hamis' ")
        print("\nElső input kiértékelve: {f}".format(f=first))
        print("Második input kiértékelve: {s}".format(s=second))
    elif first == False and second == True:
        print("Teljesül a feltétel miszerint az egyik érték 'Igaz' a másik 'Hamis' ")
        print("\nElső input kiértékelve: {f}".format(f=first))
        print("Második input kiértékelve: {s}".format(s=second))
    else:
        print("Nem teljesül a feltétel miszerint az egyik érték 'Igaz' a másik 'Hamis' ")
        print("\nElső input kiértékelve: {f}".format(f=first))
        print("Második input kiértékelve: {s}".format(s=second))


def main():
    str1 = "python"
    str2 = None
    print("A két változó értéke: {s1} és {s2}".format(s1=str1, s2=str2))
    xor(str1,str2)

    print("-------------------------------------------\n")
    str3 = "alma"
    str4 = [1, 2]
    print("A két változó értéke: {s3} és {s4}".format(s3=str3, s4=str4))
    xor(str3,str4)
    
    print("-------------------------------------------\n")
    str5 = ()
    str6 = ('Total Recall', 1990, 7.5)
    print("A két változó értéke: {s5} és {s6}".format(s5=str5, s6=str6))
    xor(str5,str6)

##############################################################################

if __name__ == "__main__":
    main()
