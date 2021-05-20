#!/usr/bin/env python3

class Verem:
    mark = "["
    
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
            return self.data.pop()
        else:
            return None

    def meret(self):
        return len(self.data)
    
    def __str__(self):
        if self.data:
            res = ""
            for elem in self.data:
                res = res + str(elem) + " "
            return "{m}{r}".format(m = Verem.mark, r = res)
        else:
            return "{}".format(Verem.mark)
            
    

def main():
    v = Verem()
    print("Üres verem létrehozva:", v)   # üres verem létrehozása
    print("Üres-e a verem:", v.ures())   # [
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print("Verem tartalma:", v)          # True
    print("Verem mérete:", v.meret())    # 3
    print("Üres-e a verem:", v.ures())   # False
    x = v.kivesz()
    print("Kivett elem:", x)             # 5
    print("Verem tartalma:", v)          # [1 4
    v.kivesz()
    v.kivesz()                           # most már üres
    x = v.kivesz()
    print("Üres veremből akartál kivenni elemet:", x)  # None

##############################################################################

if __name__ == "__main__":
    main()