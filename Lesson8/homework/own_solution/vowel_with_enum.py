#!/usr/bin/env python3
from enum import Enum, auto

class Harmony(Enum):
    MELY = auto()
    MAGAS = auto()
    VEGYES = auto()
    SEMMILYEN = auto()

class Vowel(Enum):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'

#lehet olyan konstruktor kell ami csak létrehoz egy listát, vagy kezel egy listát

class VowelHarmony:
    magas = 0
    mely = 0
    
    def result(self, word):
        self.word = word
        VowelHarmony.magas = 0
        VowelHarmony.mely = 0
        for s in self.word:
            if s in Vowel.MELY_MGHK.value:
                VowelHarmony.mely += 1
            if s in Vowel.MAGAS_MGHK.value:
                VowelHarmony.magas += 1
        if VowelHarmony.magas != 0 and VowelHarmony.mely != 0:
            return Harmony.VEGYES.value
        elif VowelHarmony.magas != 0 and VowelHarmony.mely == 0:
            return Harmony.MAGAS.value
        elif VowelHarmony.magas == 0 and VowelHarmony.mely != 0:
            return Harmony.MELY.value
        else:
            return Harmony.SEMMILYEN.value

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    vowel = VowelHarmony()
    print()
    for word in words:
        res = vowel.result(word)
        if res == Harmony.MELY.value:
            print("{w} -> mély hangrendű".format(w = word))
        elif res == Harmony.MAGAS.value:
            print("{w} -> magas hangrendű".format(w = word))
        elif res == Harmony.VEGYES.value:
            print("{w} -> vegyes hangrendű".format(w = word))
        else:
            print("{w} -> semmilyen hangrendű".format(w = word))
           

##############################################################################

if __name__ == "__main__":
    main()
