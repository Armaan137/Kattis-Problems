# This problem can be found here: https://open.kattis.com/problems/batterup.

def main():
    _ = int(input())
    hits = list(map(int, input().split(" ")))

    top = bottom = 0
    for hit in hits:
        if hit >= 0:
            top += hit
            bottom += 1

    slugging = top / bottom

    print(slugging)


if __name__ == '__main__':
    main()
