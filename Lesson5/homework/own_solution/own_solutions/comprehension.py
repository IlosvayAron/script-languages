#!/usr/bin/env python3


def ex_1():
    """
    Nagybetűsé alakítja egy string elemű lista elemeit hozzáfüzve minden elemhez a ! jelet.
    """
    words = ['auto', 'villamos', 'metro']
    result = [w.upper() + '!' for w in words]
    print("1.", words, end=" -> ")
    print(result)


def ex_2():
    """
    Nagybetűsé alakítja egy string elemű lista elemeinek az első karakterét.
    """
    words = ['aladar', 'bela', 'cecil']
    result = [w.capitalize() for w in words]
    print("2.", words, end=" -> ")
    print(result)


def ex_3():
    """
    Előállít egy 10 elemű listát csupa 0-val.
    """
    result = [0 for i in range(10)]
    print("3.", result)


def ex_4():
    """
    A lista elemeit felhasználva előállítja a páros számokat 2-től 20-ig.
    """
    numbers = list(range(1, 10+1))
    result = [n*2 for n in numbers]
    print("4.", numbers, end=" -> ")
    print(result)


def ex_5():
    """
    A string-eket tartalmazó lista elemeiből számokat állít elő.
    """
    strings = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    result = [int(s) for s in strings]
    print("5.", strings, end=" -> ")
    print(result)


def ex_6():
    """
    Adott egy számokból álló string. Ellőállít egy listát melynek elemei a string számjegyei.
    """
    string = "1234567"
    result = [int(s) for s in string]
    print("6.", string, end=" -> ")
    print(result)


def ex_7():
    """
    Egy mondat szavainak a hosszát számolja meg, majd listát képez belőlük.
    """
    sentence = 'The quick brown fox jumps over the lazy dog'
    words = sentence.split()
    result = [len(w) for w in words]
    print("7.", sentence, end=" -> ")
    print(result)


def ex_8():
    """
    Egy sztring szavainak a kezdőbetűit gyűjti össze egy listában.
    """
    sentence = "python is an awesome language"
    words = sentence.split()
    result = [w[0] for w in words]
    print("8.", sentence, end=" -> ")
    print(result)


def ex_9():
    """
    Tuple-öket helyezz el egy listában a következő szerkezettel: (szó, szóhossz).
    """
    sentence = 'The quick brown fox jumps over the lazy dog'
    words = sentence.split()
    result = [(w, len(w)) for w in words]
    print("9.", sentence, end=" -> ")
    print(result)


def ex_10():
    """
    Előállítja egy listában a 10-nél kisebb páros számokat.
    """
    result = [n for n in range(10+1) if n % 2 == 0 and n < 10]
    print("10. 10-nél kisebb páros számok: {r}".format(r=result))


def ex_11():
    """
    A 20-nál kisebb számok négyzetét állítja elő és a párosakat egy listába gyűjti.
    """
    result = [n*n for n in range(20+1) if n % 2 == 0 and n < 20]
    print("11. 20-nál kisebb számok négyzete: {r}".format(r=result))


def ex_12():
    """
    Számok listáját állítja elő.

    Előállítja a 20-nál kisebb számok négyzetét.
    Majd ezen négyzetszámok közül csak azokat
    hagyja meg, melyeknek az utolsó számjegye "4".
    A szürőn átment számokat egy listába gyűjti.
    """
    numbers = [d*d for d in range(20+1) if d < 20]
    result = [n for n in numbers if (n % 10) == 4]
    print("12. 4-re végződő 20-nál kisebb számok négyzete: {r}".format(r=result))


def ex_13():
    """
    Összegyűjti az angol ábécé nagybetűit egy listában, majd összefűzzi az elemeket egyetlen sztringgé.
    """
    letters = [chr(n).upper() for n in range(97,122+1)]
    result = "".join(letters)
    print("13. Eredmégy: {r}".format(r=result))


def ex_14():
    """
    A listában lévő szavak elejéről és végéről eltávolítja a whitespace karaktereket.
    """
    words = [' apple ', ' banana ', ' kiwi']
    result = [w.strip() for w in words]
    print("14.", words, end=" -> ")
    print(result)


def ex_15():
    """
    A listában lévő számjegyeket összefüzzi egy sztringgé.
    """
    numbers = [1, 0, 1, 1, 0, 1, 0, 0]
    strings = [str(n) for n in numbers]
    result = "".join(strings)
    print("15.", numbers, end=" -> ")
    print(result)


def main():
    ex_1()
    print('-' * 50)
    ex_2()
    print('-' * 50)
    ex_3()
    print('-' * 50)
    ex_4()
    print('-' * 50)
    ex_5()
    print('-' * 50)
    ex_6()
    print('-' * 50)
    ex_7()
    print('-' * 50)
    ex_8()
    print('-' * 50)
    ex_9()
    print('-' * 50)
    ex_10()
    print('-' * 50)
    ex_11()
    print('-' * 50)
    ex_12()
    print('-' * 50)
    ex_13()
    print('-' * 50)
    ex_14()
    print('-' * 50)
    ex_15()
    print('-' * 50)

##############################################################################

if __name__ == "__main__":
    main()
