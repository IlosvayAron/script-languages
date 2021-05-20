#!/usr/bin/env python3

def get_movie_info():
    # T.f.h. visszaakarunk adni egy adatbázisból egy rekordot(sort)
    return ('Total Recall', 1990, 7.5) 


def main():
    """
    t = get_movie_info()
    print(t)
    # Elemek kiíratása külön-külön
    title = t[0]
    year = t[1]
    score = t[2]
    print(title, year, score)
    """
    # Egy szebb változat
    title, year, score = get_movie_info() # value unpacking(érték kibontás)
    print(title, year, score)

# A 'value unpacking' listára is működik(6. sor): return ['Total Recall', 1990, 7.5]
##############################################################################

if __name__ == "__main__":
    main()