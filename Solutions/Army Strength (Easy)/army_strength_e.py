# This problem can be found here: https://open.kattis.com/problems/armystrengtheasy.

def main():
    t = int(input().strip())

    for _ in range(t):
        _ = input()
        _, _ = map(int, input().split(" "))
        g = list(map(int, input().split(" ")))
        mg = list(map(int, input().split(" ")))

        while g and mg:
            min_g = min(g)
            min_mg = min(mg)

            if min_g >= min_mg:
                mg.remove(min_mg)
            else:
                g.remove(min_g)

        if g:
            print("Godzilla")
        elif mg:
            print("MechaGodzilla")
        else:
            print("uncertain")


if __name__ == '__main__':
    main()
