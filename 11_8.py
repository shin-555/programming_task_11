from collections import Counter
import random
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = UPPER.lower()
SYMBOLS = ' -!\"&\'()*,.:;[]_`?\n'
NUMBERS = '0123456789'
str_list = UPPER+LOWER+NUMBERS+SYMBOLS  # len=81
str_list = str_list*2

table = str.maketrans(SYMBOLS+NUMBERS, ('0'*len(SYMBOLS+NUMBERS)))


def euclid(x, y):
    store_x = 1

    while(store_x != 0):
        store_x = y % x
        store_y = x
        x = store_x
        y = store_y
        gcd = store_y

    return gcd


def decode(encoded, afin, str_list):
    decoded = ''
    for i in range(len(encoded)):
        for k in range(int(len(str_list)/2)):
            if encoded[i] == afin[k]:
                decoded = decoded+str_list[k]

    return decoded


def ex_euclid(a, b):
    x, y, lastx, lasty = 0, 1, 1, 0
    while(b != 0):
        q = a//b
        a, b = b, a % b
        x, y, lastx, lasty = lastx-q*x, lasty-q*y, x, y

    return lastx


def chk_ratio(chk_txt, wordlist):
    chk_txt = chk_txt.translate(table)
    chk_txt = chk_txt.split('0')
    count = 0
    c = Counter(chk_txt)
    common = list(set(c.keys()) & set(wordlist))
    count = sum(v for k, v in c.items() if k in common)

    # for word in chk_txt:
    #   if word in wordlist:
    #      count += 1

    return count/len(chk_txt)


def main():
    N = int(len(str_list)/2)+1
    afin = []

    with open('english_wordlist.txt') as f:
        wordlist = f.read()
    f.close()

    with open('enc_wc.txt') as f:
        chk_txt = f.read()
    f.close()

    wordlist = wordlist.lower()
    wordlist = wordlist.split('\n')

    chk_txt = chk_txt.lower()
    chk_txt = [x for x in chk_txt if x != '']

    rate = 0

    for a in range(2, N):
        if euclid(a, N) == 1:
            for b in range(1, N):
                for i in range(int(len(str_list)/2)):
                    afin.append(str_list[(a*i+b) % N])

                store_txt = decode(chk_txt, afin, str_list)
                store_rate = chk_ratio(store_txt, wordlist)

                if store_rate > rate:
                    rate = store_rate
                    text = store_txt
                    store_a = a
                    store_b = b
    print(text)

    print('ratio : ', rate, 'a : ', store_a, 'b : ', store_b)


if __name__ == "__main__":
    main()
