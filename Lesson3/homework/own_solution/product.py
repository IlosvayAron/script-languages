#!/usr/bin/env python3


def product(lst):
    result = 1
    for e in lst:
        result = result * e
    print('A lista elemeinek a szorzata: {0}'.format(result)) 


def elements_of_list(lst):
    res = []
    for e in lst:
        res.append(e)
    print('A lista elemei: {0}'.format(res))

     
def main():
    lst = [1,2,3,4,5]
    lsst = []
    elements_of_list(lst)
    product(lst)
    elements_of_list(lsst)
    product(lsst)
    
    
if __name__ == "__main__":
    main()
