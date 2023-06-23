# This problem can be found here: https://open.kattis.com/problems/tarifa.

def main():
    x = int(input())
    n = int(input())

    ans = x
    for _ in range(n):
        p = int(input())
        ans += (x - p)

    print(ans)


if __name__ == "__main__":
    main()
