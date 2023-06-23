# This problem can be found here: https://open.kattis.com/problems/qaly.

def main():
    n = int(input())

    ans = 0
    for _ in range(n):
        q, y = list(map(float, input().split(" ")))
        ans += q * y

    print(ans)


if __name__ == "__main__":
    main()
