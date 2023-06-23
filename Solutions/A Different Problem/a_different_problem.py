# This problem can be found here: https://open.kattis.com/problems/different.

def main():
    while True:
        try:
            a, b = list(map(int, input().split(" ")))
            diff = abs(a - b)
            print(diff)
        except EOFError:
            break


if __name__ == "__main__":
    main()
