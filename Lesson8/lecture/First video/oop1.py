#!/usr/bin/env python3

class EmptyClass:
    pass


class MyClass:
    def hello(self):
        return "Hello world!"



def main():
    obj = MyClass()
    print(obj.hello())

##############################################################################

if __name__ == "__main__":
    main()