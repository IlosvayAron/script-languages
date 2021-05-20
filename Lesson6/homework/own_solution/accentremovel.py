#!/usr/bin/env python3

TEXT ="""
\"A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.\"
"""

STRING_ACCENT_LETTERS = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
LETTERS = "aeiouAEIOU"
DIC_ACCENT_LETTERS = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ö':'o', 'ő':'o', 'ú':'u', 'ü': 'u',
'ű':'u', 'Á':'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ö':'O', 'Ő':'O', 'Ú':'U', 'Ü':'U', 'Ű':'U'}


def replace_accent(text, data_structures=STRING_ACCENT_LETTERS):
    i = 0
    if data_structures == STRING_ACCENT_LETTERS:
        for d in data_structures:
            if d == 'ó' or d == 'ö' or d == 'ő':
                i = 3
                text = text.replace(d,LETTERS[i])
                continue
            elif d == 'ú' or d == 'ü' or d == 'ű':
                i = 4 
                text = text.replace(d,LETTERS[i])
                continue
            elif d == 'Ó' or d == 'Ö' or d == 'Ő':
                i = len(LETTERS) - 2
                text = text.replace(d,LETTERS[i])
                continue
            elif d == 'Ú' or d == 'Ü' or d == 'Ű':
                i = len(LETTERS) - 1
                text = text.replace(d,LETTERS[i])
                continue
            elif i == 4:
                i += 1
            else:
                text = text.replace(d,LETTERS[i])
                i += 1
    else:
        keys = data_structures.keys()
        values = data_structures.values()
        for k in data_structures.keys():
            text = text.replace(k,data_structures[k])
    return text


def main():
    text1 = replace_accent(TEXT)
    text2 = replace_accent(TEXT, data_structures=DIC_ACCENT_LETTERS)
    print('Naiv megközelités:')
    print(text1)
    print('-' * 60)
    print('Dictionary használata:')
    print(text2)

##############################################################################

if __name__ == "__main__":
    main()