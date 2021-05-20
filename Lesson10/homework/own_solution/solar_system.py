#!/usr/bin/env python3

def main():
    with open("DT2.csv", 'r') as f:
        words = []
        for string in f.read().splitlines():
            words.append(string.split(",")[0])
        #print(words)
        result = []
        for w in words:
            u = w.upper()
            if u.find("J") != -1 and u.find("S") != -1 and u.find("U") != -1 and u.find("N") != -1:
               if u.find("J") < u.find("S") < u.find("U") < u.find("N"):
                   result.append(w)
        print("Segítség a bolygók nevének megjegyzéséhez:", result)

##############################################################################

if __name__ == "__main__":
    main()
