#!/usr/bin/env python3


def greet(name, greetings='Hello'):
    print(f'{greetings} {name}!')


def main():
    greet('Aron')
    greet('Aron', greetings='Hola')
    greet('Aron', greetings='Bonjour')

##############################################################################

if __name__ == "__main__":
    main()