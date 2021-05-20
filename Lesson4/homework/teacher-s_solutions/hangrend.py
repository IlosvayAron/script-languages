#!/usr/bin/env python3

MELY, MAGAS, VEGYES, SEMMILYEN = range(1,5)
MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'

def hangrend(szo):
    magas = 0
    mely = 0
    for s in szo:
        if s in MELY_MGHK:
            mely += 1
        if s in MAGAS_MGHK:
            magas += 1
    if magas != 0 and mely != 0:
        return VEGYES
    elif magas != 0 and mely == 0:
        return MAGAS
    elif magas == 0 and mely != 0:
        return MELY
    else:
        return SEMMILYEN


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for word in words:
        hr = hangrend(word)
        if hr == MELY:
            print("{w} -> mély hangrendű".format(w = word))
        elif hr == MAGAS:
            print("{w} -> magas hangrendű".format(w = word))
        elif hr == VEGYES:
            print("{w} -> vegyes hangrendű".format(w = word))
        else:
            print("{w} -> semmilyen hangrendű".format(w = word))

##############################################################################

if __name__ == "__main__":
    main()