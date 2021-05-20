#!/usr/bin/env python3

def is_anagram_not_trivial(text_1, text_2):
    print(f"A viszgálandó szavak/szöveg: '{text_1}', '{text_2}'")
    text_1 = text_1.lower().split()
    text_2 = text_2.lower().split()
    d1 = dict()
    for word in text_1:
        for w in word:
            if w not in d1:
                d1[w] = 1
            else:
                d1[w] += 1
    print('-' * 40)
    d2 = dict()
    for word in text_2:
        for w in word:
            if w not in d2:
                d2[w] = 1
            else:
                d2[w] += 1
    result = False
    if len(d2) == len(d1):
        for k in sorted(d2.keys()):
            if d2[k] == d1[k]:
                result = True            
            else:
                return result
    else:
        return result
    return result


def is_anagram_trivial(text_1, text_2):
    print(f"A két szó/szöveg: '{text_1}', '{text_2}'")
    text_1 = text_1.lower().split()
    text_2 = text_2.lower().split()
    text_1 = ''.join(text_1)
    text_2 = ''.join(text_2)
    text_1 = sorted(text_1)
    text_2 = sorted(text_2)
    if text_1 == text_2:
        print("A két szó/szöveg anagramma!")
    else:
        print("A két szó/szöveg nem anagramma!")


def main():
    print("Triviális módszer!")
    is_anagram_trivial("Conversation", "Voices rant on")
    print('-' * 40)
    is_anagram_trivial("Clint Eastwood", "Old west action")
    print('-' * 40)
    is_anagram_trivial("reentrance", "INTERFERANCE")
    print('-' * 40)
    is_anagram_trivial("To much SaLtY food", "IS bad For you")
    print()
    print("Nem triviális módszer!")
    print("Anagramma? ->", is_anagram_not_trivial("Conversation", "Voices rant on"))
    print('-' * 40)
    print("Anagramma? ->", is_anagram_not_trivial("Clint Eastwood", "Old west action"))
    print('-' * 40)
    print("Anagramma? ->", is_anagram_not_trivial("reentrance", "INTERFERANCE"))
    print('-' * 40)
    print("Anagramma? ->", is_anagram_not_trivial("To much SaLtY food", "IS bad For you"))

####s##########################################################################

if __name__ == "__main__":
    main()