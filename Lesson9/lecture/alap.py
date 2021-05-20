#!/usr/bin/env python3
import mymod

def main():
    # Kérdés: mit add vissza a fv? int, str, float, lista, halmaz stb.?
    # Naiv megközelités: megnyitom a modul kódját és megkeresem a fv.-t.
    # Az ilyen esetekre jó az annotáció: a modulban a fv. annotálva van
    # akkor a elegendő csak a fv. nevét megnéznem mivel ott van annotálva.
    result: int = mymod.get_result()

##############################################################################

if __name__ == "__main__":
    main()