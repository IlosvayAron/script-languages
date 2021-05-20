#!/usr/bin/env python3

class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def getWidth(self, width):
        return self.width
    
    def setWidth(self, width):
        self.width = width
    
    def getHeight(self, height):
        return self.height
    
    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.getWidth(self.width) * self.getHeight(self.height)

def main():
    rect = Rectangle(50, 10)
    print(rect.area())
    rect.setWidth(60)
    print(rect.area())

##############################################################################

if __name__ == "__main__":
    main()