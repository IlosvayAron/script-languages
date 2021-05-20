#!/usr/bin/env python3


def loop(number, debug=False):
    """
    Számok egy sorozatát adja vissza.

    Két paraméterrel rendelkezik. Az első paramétere a 'number',
    ez az az érték ameddig kiakarjuk íratni a számokat. A második
    paraméter opcionális, a 'debug'. Ha nem kap értéket akkor csak
    egyszerűen kiírja a számokat 1-től number-ig. Ha azonban a 
    'debug = True' értéket adjuk meg akkor a következő lesz a kimenet:
    
    # ciklus kezdete
    számok sorozata 1-től number-ig
    # ciklus vége
    """
    print(f'A számok 1-től {number}-ig:')
    if debug:
        print('# ciklus kezdete')
        for n in range(1, number+1):
            print(f'{n}', end=' ')
        print('\n# ciklus vége')
    else:
        for n in range(1, number+1):
            print(f'{n}', end=' ')
    print()


def main():
    loop(30)
    print('-' * 40)
    loop(5, debug=True)

##############################################################################

if __name__ == "__main__":
    main()