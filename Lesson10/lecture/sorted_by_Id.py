#!/usr/bin/env python3

"""
    Legyen adott a köv. lista:
    
    lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']

    Rendezzük a listát user ID szerint csökkenő sorrendbe:

        100:User3
        80:User2
        75:User4
        45:User5
        10:User1
        00:User4
"""

#def sorted_by_id(user):
#    return int(user.split(":")[0])

def main():
    lst = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print("Eredeti lista:", lst)
    print("Rendezve ID szerint:", sorted(lst, key=lambda user: int(user.split(":")[0]), reverse=True))

##############################################################################

if __name__ == "__main__":
    main()