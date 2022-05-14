

def main():
    store_x = 1
    y = 38
    x = 120

    print("x = ",x,"y = ",y)

    while(store_x != 0):
        store_x = y % x
        store_y = x
        x = store_x
        y = store_y
        gcd = store_y

    print("gcd = ",gcd)


if __name__ == "__main__":
    main()
