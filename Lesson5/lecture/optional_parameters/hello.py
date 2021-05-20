#!/usr/bin/env python3


def hello(name, repeat=1, postfix=''):
    for i in range(repeat):
        print(name + postfix) #or print(f'{name}{postfix}')


def main():
    hello('Aron')
    print('-' * 40)
    hello('Aron', repeat=3)
    print('-' * 40)
    hello('Aron', repeat=2, postfix='!')
    print('-' * 40)
    hello('Aron', 4, '!!')

##############################################################################

if __name__ == "__main__":
    main()