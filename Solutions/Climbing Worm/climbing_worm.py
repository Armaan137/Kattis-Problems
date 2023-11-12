# This problem can be found here: https://open.kattis.com/problems/climbingworm.

def main():
    a, b, h = map(int, input().split())

    i = cnt = 0
    while True:
        cnt += 1
        i += a
        if i >= h:
            break
        i -= b

    print(cnt)


if __name__ == '__main__':
    main()
