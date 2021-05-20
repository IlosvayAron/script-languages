#!/usr/bin/env python3

#2)Iteratív módszer
def iter_palindrom(s):
    i = len(s)
    j = 0
    while (i > 0 and j != i):
        if s[j] == s[i-1]:
            i -= 1
            j += 1
        else:
            return False
    return True

    
#3)Rekurzív módszer
def rek_palindrom(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return rek_palindrom(s[1:-1])
        else:
            return False


def main():
    print('Palindrom vagy sem?')
    s1 = 'alma'
    s2 = 'görög'
    print('Első szó:',s1)
    print('Iteratív módszer: {}'.format(iter_palindrom(s1)))
    print('Rekurzív módszer: {}'.format(rek_palindrom(s1)))
    print('Második szó:',s2)
    print('Iteratív módszer: {}'.format(iter_palindrom(s2)))
    print('Rekurzív módszer: {}'.format(rek_palindrom(s2)))
    
if __name__ == "__main__":
    main()
