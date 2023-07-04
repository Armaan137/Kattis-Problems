# This problem can be found here: https://open.kattis.com/problems/hangingout.

def main():
    l, x = map(int, input().split(" "))

    ans = terrace = 0
    for _ in range(x):
        event, p = input().split(" ")
        if event == "enter" and terrace + int(p) <= l:
            terrace += int(p)
        elif event == "enter" and terrace + int(p) > l:
            ans += 1
        elif event == "leave":
            terrace -= int(p)

    print(ans)


if __name__ == '__main__':
    main()
