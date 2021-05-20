#!/usr/bin/env python3
from typing import List


def median(lst: List[float]) -> float:
    lst.sort()
    if len(lst) % 2 != 0:
        halves = len(lst) // 2
        median = lst[halves]
    else:
        first_element = len(lst) // 2 - 1
        second_element = len(lst) // 2 
        median = (lst[first_element] + lst[second_element]) / 2
    return median


def main() -> None:
    first = median([1, 2, 3, 4, 5])
    second = median([3, 1, 2, 5, 3])
    third = median([1, 300, 2, 200, 1])
    fourth = median([3, 6, 20, 99, 10, 15])
    print("A listák mediánja!")
    print("[1, 2, 3, 4, 5] = ", first)
    print("[3, 1, 2, 5, 3] = ", second)
    print("[1, 300, 2, 200, 1] = ", third)
    print("[3, 6, 20, 99, 10, 15] = ", fourth)

##############################################################################

if __name__ == "__main__":
    main()