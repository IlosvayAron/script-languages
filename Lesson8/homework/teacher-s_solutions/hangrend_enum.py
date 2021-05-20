# #!usr/bin/env python
from enum import Enum, auto

magas_mghk = 'eéiíöőüű'
mely_mghk = 'aáoóuú'

class Hangrend(Enum):
    MELY = auto()
    MAGAS = auto()
    VEGYES = auto()
    SEMMILYEN = auto()


def hangrend(word):
    magas = mely = False
    for c in word:
        if c in magas_mghk:
            magas = True
        elif c in mely_mghk:
            mely = True
    if magas and mely:
        return Hangrend.VEGYES
    elif magas:
        return Hangrend.MAGAS
    elif mely:
        return Hangrend.MELY
    else:
        return Hangrend.SEMMILYEN
    
def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mely", "pff"]
    for w in words:
        hr = hangrend(w)
        text = ""
        if hr == Hangrend.MELY:
            text = "mély"
        elif hr == Hangrend.MAGAS:
            text = "magas"
        elif hr == Hangrend.VEGYES:
            text == "vegyes"
        else:
            text = "semmilyen"
        print('{} -> {}'.format(w, text))

##############################################################
if __name__ == '__main__':
    main()
