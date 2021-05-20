#!/usr/bin/env python3

# A program a kisbetűkkel leírt film címet kiírja helyesen a megfelelő
# helyeken nagybetüvel


def main() -> None:
    s = input("Add meg egy film címét kisbetükkel: ")
    print("A film címe helyesen: " + s.title())
    
    
if __name__ == "__main__":
    main()
