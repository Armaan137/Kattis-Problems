# This problem can be found here: https://open.kattis.com/problems/basicprogramming1.

def main():
    n, t = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))

    if t == 1:
        print("7")
    elif t == 2:
        case_two(a)
    elif t == 3:
        case_three(a)
    elif t == 4:
        case_four(a)
    elif t == 5:
        case_five(a)
    elif t == 6:
        case_six(a)
    else:
        case_seven(n, a)


def case_two(array):
    a, b = array[0], array[1]

    if a > b:
        print("Bigger")
    elif a == b:
        print("Equal")
    else:
        print("Smaller")


def case_three(array):
    a, b, c = array[0], array[1], array[2]

    print(sorted([a, b, c])[1])


def case_four(array):
    print(sum(array))


def case_five(array):
    cnt = 0

    for n in array:
        if n % 2 == 0:
            cnt += n

    print(cnt)


def case_six(array):
    print("".join(chr(97 + (i % 26)) for i in array))


def case_seven(n, array):
    seen = set()
    i = 0
    seen.add(i)

    while True:
        i = array[i]

        if i > n - 1:
            print("Out")
            break
        elif i == n - 1:
            print("Done")
            break
        elif i in seen:
            print("Cyclic")
            break

        seen.add(i)


if __name__ == '__main__':
    main()
