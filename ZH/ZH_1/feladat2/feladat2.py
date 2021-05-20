#!/usr/bin/env python3

def main():
    f = open("input.txt", "r")
    text = f.read()
    f.close()
    cel = -1
    legmagasabb = 0
    legmélyebb = 0
    for t in text:
        if t == '(':
            cel += 1
            legmagasabb += 1
        else:
            cel -= 1
            legmélyebb -= 1 
    print(f'Cél emelet: {cel}')
    print(f'Legmagasabb emelet: {legmagasabb}')
    print(f'Legmélyebb emelet: {legmélyebb}')


##############################################################################

if __name__ == "__main__":
    main()