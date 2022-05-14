SYMBOLS = ' -!\"&\'()*,.:;[]_`?\n'
NUMBERS = '0123456789'

table = str.maketrans(SYMBOLS+NUMBERS, ('0'*len(SYMBOLS+NUMBERS)))


def chk_ratio(chk_txt, wordlist):
    chk_txt = chk_txt.translate(table)
    chk_txt = chk_txt.split('0')
    count = 0

    for i in range(len(chk_txt)):
        for l in range(len(wordlist)):
            if chk_txt[i] == wordlist[l]:
                count += 1

    return count/len(chk_txt)


def main():
    with open('english_wordlist.txt') as f:
        wordlist = f.read()
    f.close()

    with open('check_list.txt') as f:
        chk_txt = f.read()
    f.close()

    wordlist = wordlist.lower()
    wordlist = wordlist.split('\n')

    chk_txt = chk_txt.lower()

    result_ratio = chk_ratio(chk_txt, wordlist)

    print(result_ratio)


if __name__ == "__main__":
    main()
