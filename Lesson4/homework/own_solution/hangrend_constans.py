# #!usr/bin/env python

magas_mghk = 'eéiíöőüű'
mely_mghk = 'aáoóuú'

MELY = 0
MAGAS = 1
VEGYES = 2
SEMMILYEN = 3


def hangrend(word):
    magas = mely = False
    for c in word:
        if c in magas_mghk:
            magas = True
        elif c in mely_mghk:
            mely = True
    #
    if magas and mely:
        return VEGYES
    elif magas:
        return MAGAS
    elif mely:
        return MELY
    else:
        return SEMMILYEN
    
def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mely", "pff"]
    for w in words:
        hr = hangrend(w)
        text = ""
        if hr == MELY:
            text = "mély"
        elif hr == MAGAS:
            text = "magas"
        elif hr == VEGYES:
            text == "vegyes"
        else:
            text = "semmilyen"
        print('{} -> {}'.format(w, text))

##############################################################
if __name__ == '__main__':
    main()
