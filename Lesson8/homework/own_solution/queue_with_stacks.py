#!/usr/bin/env python3

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append(self, value):
        self.stack1.append(value)

    def popleft(self):
        for v in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def is_empty(self):
        if len(self.stack2) == 0:
            return True
        else:
            return False
        
    def size(self):
        if self.stack2:
            return len(self.stack2)
        else:
            return len(self.stack1)

    def __str__(self):
        if self.stack1:
            return "{s}".format(s = self.stack1)
        else:
            return "{}".format(self.stack1)

def main():
    q = MyQueue()
    q.append(5)
    q.append(10)
    q.append(15)
    q.append(20)
    print("Sor tartalma:", q)
    print("Az elemek száma:", q.size())
    print("Kivett elem:", q.popleft())
    print("Kivett elem:", q.popleft())
    print("Üres-e a sor:", q.is_empty())
    print("Az elemek száma:", q.size())
    print("Kivett elem:", q.popleft())
    print("Kivett elem:", q.popleft())
    print("Üres-e a sor:", q.is_empty())
    print("Az elemek száma:", q.size())


##############################################################################

if __name__ == "__main__":
    main()