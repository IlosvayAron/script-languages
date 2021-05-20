#!/usr/bin/env python3

def clear_string(text):
    if ' ' in text:
        text = text.replace(' ', '')
        print('Whitespace karakter nélküli: "{0}"'.format(text))


def main():
    text = '192. 20. 246. 138: 6666'
    print('Eredeti string: "{t}"'.format(t=text))
    clear_string(text)


if __name__ == "__main__":
    main()