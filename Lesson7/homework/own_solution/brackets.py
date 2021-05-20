#!/usr/bin/env python3

def test(text):
    lst = ['(', ')', '[', ']', '{', '}']
    new_lst = []
    for t in text:
        if t in lst:
            new_lst.append(t)
    i = 0
    stack = []
    while i < len(new_lst):
        #print(text[i], end=' ')
        if (new_lst[i] == '(' or new_lst[i] == '[' or new_lst[i] == '{'):
            stack.append(new_lst[i])
        else:
            if stack == []:
                return False
            if new_lst[i] == ')' and stack[-1] != '(' or new_lst[i] == ']' and stack[-1] != '[' or new_lst[i] == '}' and stack[-1] != '{':
                return False
            stack.pop()
        i += 1
    if stack == []:
        return True
    else:
        return False


def main():
    print("Helyes-e a kifejezés vagy sem?")
    print( "((5+3)*2+1) ->", test("((5+3)*2+1)")) # True
    print("{[(3+1)+2]+} -> ", test("{[(3+1)+2]+}"))  # True
    print("(3+{1-1)} ->", test("(3+{1-1)}"))  # False
    print("[1+1]+(2*2)-{3/3} ->", test("[1+1]+(2*2)-{3/3}"))  # True
    print("(({[(((1)-2)+3)-3]/3}-3) ->", test("(({[(((1)-2)+3)-3]/3}-3)"))  # False

##############################################################################

if __name__ == "__main__":
    main()