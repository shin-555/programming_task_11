from collections import Counter
import collections
import random
import time
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = UPPER.lower()
SYMBOLS = ' -!\"&\'()*,.:;[]_`?\n'
NUMBERS = '0123456789'
STR_LIST = UPPER+LOWER+NUMBERS+SYMBOLS  # len=81
str_list = STR_LIST*2
N = len(STR_LIST)

table = str.maketrans(SYMBOLS+NUMBERS, ('0'*len(SYMBOLS+NUMBERS)))


def gcd(x, y):
    store_x = 1

    while(store_x != 0):
        store_x = y % x
        store_y = x
        x = store_x
        y = store_y
        gcd = store_y

    return gcd


def euclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    a1 = a
    b1 = b
    while b1 != 0:
        c, a1, b1 = a1 // b1, b1, a1 % b1
        x0, x1 = x1, x0 - c * x1
        y0, y1 = y1, y0 - c * y1

    if a1 != 1:
        return -1
    else:
        return x0 % b


def decode(encoded, a, b):
    x = euclid(a, len(STR_LIST))

    decoded = ''
    for i in encoded:
        decoded += STR_LIST[(x*(STR_LIST.find(i)-b)) % len(STR_LIST)]
    return decoded


def ex_euclid(a, b):
    x, y, lastx, lasty = 0, 1, 1, 0
    while(b != 0):
        q = a//b
        a, b = b, a % b
        x, y, lastx, lasty = lastx-q*x, lasty-q*y, x, y

    return lastx


def chk_ratio(chk_txt, wordlist):
    chk_txt = chk_txt.lower()

    chk_txt = chk_txt.translate(table)
    chk_txt = chk_txt.split('0')
    count = 0

    c = Counter(chk_txt)
    common = list(set(c.keys()) & set(wordlist))
    count = sum(v for k, v in c.items() if k in common)

    return count/len(chk_txt)


def estimate(top_de, top_en, second_de, second_en):
    for a in range(N):
        for b in range(N):
            if top_en == (a*top_de+b) % N and second_en == (a*second_de+b) % N:
                return a, b
    return 0, 0


def main():
    frag = int(input('8 or 9 : '))
    start_time = time.time()

    with open('english_wordlist.txt') as f:
        wordlist = f.read()
    f.close()

    with open('enc_wc.txt') as f:
        chk_txt = f.read()
    f.close()

    wordlist = wordlist.lower()
    wordlist = wordlist.split('\n')

    if frag == 8:
        rate = 0

        for a in range(2, N):
            if gcd(a, N) == 1:
                for b in range(1, N):
                    store_txt = decode(chk_txt, a, b)
                    store_rate = chk_ratio(store_txt, wordlist)

                    if store_rate > rate:
                        rate = store_rate
                        text = store_txt
                        max_a = a
                        store_b = b

        end_time = time.time()
        print('ratio : ', rate, 'a : ', max_a, 'b : ', store_b)
        print("time : ", end_time-start_time)

    elif frag == 9:
        store_data = collections.Counter(chk_txt)
        challacter, num = zip(*store_data.most_common())

        store_rate = 0

        for i in range(5):
            for j in range(5):
                store_1 = STR_LIST.find('e')
                store_2 = STR_LIST.find(challacter[i])
                store_3 = STR_LIST.find('a')
                store_4 = STR_LIST.find(challacter[j])

                a, b = estimate(store_1, store_2, store_3, store_4)
                decoded = decode(chk_txt, a, b)
                rate = chk_ratio(decoded, wordlist)

                if rate > store_rate:
                    store_rate = rate
                    store_decoded = decoded
                    store_a = a
                    store_b = b

        end_time = time.time()
        print('ratio : ', store_rate, 'a : ', store_a, 'b : ', store_b)
        print("time : ", end_time-start_time)


if __name__ == "__main__":
    main()
