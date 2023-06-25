# This problem can be found here: https://open.kattis.com/problems/judgingmoose.

def main():
    left, right = map(int, input().split(" "))

    if left == 0 and right == 0:
        print("Not a moose")
    elif left == right:
        print("Even", left * 2)
    else:
        print("Odd", max(left, right) * 2)


if __name__ == "__main__":
    main()
