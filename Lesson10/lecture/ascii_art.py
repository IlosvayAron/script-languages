#!/usr/bin/env python3

"""
words lista:
        Cc      Bb      aa      zz      <-- eredeti lista
        |       |       |       |
        cc      bb      aa      zz      <-- proxy lst: str.lower alkalmazása elemenként és rendezés
        aa      bb      cc      zz      <-- rendezet lista(proxy listában történik a rendezés)

        aa      Bb      Cc      zz      <-- megfelelő elemek visszahelyestessítése

letters lista:
       xc       zb      yd      wa      <-- eredeti lista
       |        |       |       |
       c        b       d       a       <-- utolsó karakter visszaadása elementként
       a        b       c       d       <-- rendezett proxy listában

       wa       zb      xc      yd      <-- eredmény a visszahelyettesítést követően

"""

def my_func(s):
    return s[-1]

def main():
    words=['Cc','Bb','aa','zz']
    print("Eredeti lista:", words)
    print("Egyszerű rendezés:", sorted(words))
    print("Rendezés 'innercase' módban:", sorted(words, key=str.lower))
    print("-" * 40)
    letters=['xc','zb','yd','wa']
    print("Eredeti lista:", letters)
    print("Rendezés utolsó betű alapján:", sorted(letters, key=my_func))

##############################################################################

if __name__ == "__main__":
    main()