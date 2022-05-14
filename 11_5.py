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


def encode(text, afin, str_list):
    encoded = []
    for i in range(len(text)):
        for k in range(int(len(str_list)/2)):
            if text[i] == str_list[k]:
                encoded.append(afin[k])
    return encoded


def decode(encoded, afin, str_list):
    decoded = []
    for i in range(len(encoded)):
        for k in range(int(len(str_list)/2)):
            if encoded[i] == afin[k]:
                decoded.append(str_list[k])
    return decoded

def ex_euclid(a, b): #拡張ユークリッドの互除法
    x, y, lastx, lasty = 0, 1, 1, 0
    l=1
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, y, lastx, lasty = lastx - q * x, lasty - q * y, x, y
        l+=1

    return lastx, lasty


def main():
    N = int(len(str_list)/2)+1
    afin = []
    text = "asdlfkj!? )"
    x=-1

    while(x<0): #xの値が正になるまで繰り返す
        while(1):
            keyA = random.randint(2, N-1)
            if euclid(keyA, N) == 1:
                break
        keyB = random.randint(1, N)

        x,y=ex_euclid(keyA,N)

    print("x = ",x)

if __name__ == "__main__":
    main()
