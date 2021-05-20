#!/usr/bin/env python3
def is_palindrom(s):
    if type(s) == str:
        return s == s[::-1]
    else:
        return str(s) == str(s)[::-1]

def dectobin(number):
    number = int(number)
    res = []
    while number // 2 != 0:
        remainder = number % 2
        number = number // 2
        res.append(str(remainder))
    res.append(str(number))
    return "".join(res[::-1])