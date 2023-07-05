# This problem can be found here: https://open.kattis.com/problems/brokenswords.

def main():
    n = int(input())

    tb = lr = 0
    for _ in range(n):
        line = input()
        for i, slat in enumerate(line):
            if slat == "0":
                if i == 0 or i == 1:
                    tb += 1
                else:
                    lr += 1

    swords = min(tb // 2, lr // 2)
    s = swords * 2

    print(swords, tb - s, lr - s)


if __name__ == '__main__':
    main()
