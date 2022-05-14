import random


def euclid(x, y):
    store_x = 1

    while(store_x != 0):
        store_x = y % x
        store_y = x
        x = store_x
        y = store_y
        gcd = store_y

    return gcd


def main():
    N = 100
    while(1): #gcdが1になるまで繰り返す
        keyA = random.randint(2, N-1)
        if euclid(keyA, N) == 1:
            break
    keyB = random.randint(1, N-1)

    print("keyA = ",keyA,"keyB = ",keyB)


if __name__ == "__main__":
    main()
