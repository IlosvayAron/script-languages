#!/usr/bin/env python3


def sum(a, b):
    sum = int(a) + int(b)
    print('A két szám összeget: {0}'.format(sum)) 


#B) Számok bekérése a felhasználótól!       
def main():
    print('Adj meg két számot!')
    a = input('Első szám: ')
    b = input('Második szám: ')
    sum(a,b)
    
    
if __name__ == "__main__":
    main()
