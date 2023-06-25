# This problem can be found here: https://open.kattis.com/problems/quadrant.

def main():
    x = int(input())
    y = int(input())

    if 0 <= x <= 1000 and 0 <= y <= 1000:
        print("1")
    elif -1000 <= x <= 0 <= y <= 1000:
        print("2")
    elif -1000 <= x <= 0 and -1000 <= y <= 0:
        print("3")
    else:
        print("4")


if __name__ == "__main__":
    main()
