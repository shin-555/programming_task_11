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


def main():
    N = int(len(str_list)/2)+1
    afin = []
    text = "asdlfkj!? )"

    while(1):
        keyA = random.randint(2, N-1)
        if euclid(keyA, N) == 1:
            break
    keyB = random.randint(1, N)

    for i in range(int(len(str_list)/2)):
        afin.append(str_list[(keyA*i+keyB) % N])

    encoded = encode(text, afin, str_list)

    print("keyA = ",keyA,"keyB = ",keyB)
    print(encoded)


if __name__ == "__main__":
    main()
