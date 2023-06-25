# This problem can be found here: https://open.kattis.com/problems/onechicken.

def main():
    n, m = map(int, input().split(" "))
    diff = abs(n - m)

    if diff == 1 and n < m:
        print(f"Dr. Chaz will have {diff} piece of chicken left over!")
    elif diff == 1 and n > m:
        print(f"Dr. Chaz needs {diff} more piece of chicken!")
    elif n < m:
        print(f"Dr. Chaz will have {diff} pieces of chicken left over!")
    elif n > m:
        print(f"Dr. Chaz needs {diff} more pieces of chicken!")


if __name__ == "__main__":
    main()
