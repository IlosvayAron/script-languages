#!/usr/bin/env python3

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # Ez a házi része volt
    def __str__(self):
        return "Rectangle({w}, {h})".format(w = self.width, h = self.height)
    #########################

def main():
    rect = Rectangle(50, 10)
    rect.width = 60
    # Ez a házi része volt
    print("Rectangle(szélleség, magasság): ", rect)
    #########################
    print("Eredmény: ", rect.area())


##############################################################################

if __name__ == "__main__":
    main()