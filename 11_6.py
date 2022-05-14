import random
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = UPPER.lower()
SYMBOLS = ' -!\"&\'()*,.:;[]_`?\n'
NUMBERS = '0123456789'
str_list = UPPER+LOWER+NUMBERS+SYMBOLS  # len=81
str_list = str_list*2


def euclid(x, y):
    store_x = 1

    while(store_x != 0):
        store_x = y % x
        store_y = x
        x = store_x
        y = store_y
        gcd = store_y

    return gcd


def encode(text, afin, str_list, j):
    encoded = []
    encode_j = []
    for i in range(len(text)):
        for k in range(int(len(str_list)/2)):
            if text[i] == str_list[k]:
                encoded.append(afin[k])
                encode_j.append(j[k])
    return encoded, encode_j


def ex_euclid(a, b):
    x, y, lastx, lasty = 0, 1, 1, 0
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, y, lastx, lasty = lastx - q * x, lasty - q * y, x, y

    return lastx


def main():
    N = int(len(str_list)/2)+1
    x = -1
    afin = []
    j = []
    store_decoded = []
    text = "asdlfkj!? )"

    while(x < 0):
        while(1):
            keyA = random.randint(2, N-1)
            if euclid(keyA, N) == 1:
                break
        keyB = random.randint(1, N)

        x = ex_euclid(keyA, N)

    print("keyA : ", keyA, "keyB : ", keyB)

    for i in range(int(len(str_list)/2)):
        afin.append(str_list[(keyA*i+keyB) % N])
        j.append((keyA*i+keyB) % N)  # 番号を記憶

    encoded, encode_j = encode(text, afin, str_list, j)
    print("afin暗号でencodeされた文字列")
    print(encoded)

    for i in range(len(encoded)):  # 11-6の方法でdecode
        store_decoded.append(str_list[(x*(encode_j[i]-keyB)) % N])

    print("11-6の式を用いてdecodeした結果")
    print(store_decoded)


if __name__ == "__main__":
    main()
