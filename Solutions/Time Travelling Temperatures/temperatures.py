# This problem can be found here: https://open.kattis.com/problems/temperature.

def main():
    a, b = map(float, input().split())
    b -= 1

    if b < 0.5:
        if a == 0:
            print("ALL GOOD")
        else:
            print("IMPOSSIBLE")
    else:
        print(-a / b)


if __name__ == "__main__":
    main()
