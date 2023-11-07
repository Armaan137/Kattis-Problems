# This problem can be found here: https://open.kattis.com/problems/ptice.

def main():
    n = int(input())
    line = input()
    adrian = ["A", "B", "C"]
    bruno = ["B", "A", "B", "C"]
    goran = ["C", "C", "A", "A", "B", "B"]

    a = b = g = 0
    for i in range(n):
        if line[i] == adrian[i % 3]:
            a += 1
        if line[i] == bruno[i % 4]:
            b += 1
        if line[i] == goran[i % 6]:
            g += 1

    m = max(a, b, g)
    print(m)

    if a == m:
        print("Adrian")
    if b == m:
        print("Bruno")
    if g == m:
        print("Goran")


if __name__ == '__main__':
    main()
