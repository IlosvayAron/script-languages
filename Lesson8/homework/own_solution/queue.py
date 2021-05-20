#!/usr/bin/env python3

class Sor:
    def __init__(self):
        self.data = []
    
    def ures(self):
        if self.data:
            return False
        else:
            return True
    
    def betesz(self, value):
        self.data.append(value)

    def kivesz(self):
        if self.data:
            return self.data.pop(0)
        else:
            return None

    def meret(self):
        return len(self.data)
    
    def __str__(self):
        if self.data:
            return "{d}".format(d = self.data)
        else:
            return "{}".format(self.data)
            
    

def main():
    s = Sor()
    print("Üres sor létrehozva:", s)   # üres sor létrehozása
    print("Üres-e a sor:", s.ures())   # [
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print("Sor tartalma:", s)          # True
    print("Sor mérete:", s.meret())    # 3
    print("Üres-e a sor:", s.ures())   # False
    x = s.kivesz()
    print("Kivett elem:", x)             # 1
    print("Sor tartalma:", s)          # [4 5
    s.kivesz()
    s.kivesz()                           # most már üres
    x = s.kivesz()
    print("Üres sorból akartál kivenni elemet:", x)  # None

##############################################################################

if __name__ == "__main__":
    main()