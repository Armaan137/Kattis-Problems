# This problem can be found here: https://open.kattis.com/problems/provincesandgold.

def main():
    g, s, c = map(int, input().split(" "))
    power = 3 * g + 2 * s + 1 * c

    victory = ""
    if power >= 8:
        victory += "Province"
    elif 5 <= power < 8:
        victory += "Duchy"
    elif 2 <= power < 5:
        victory += "Estate"

    treasure = ""
    if power >= 6:
        treasure += "Gold"
    elif 3 <= power < 6:
        treasure += "Silver"
    elif 0 <= power < 3:
        treasure += "Copper"
    if victory and treasure:
        print(f"{victory} or {treasure}")
    elif victory and not treasure:
        print(f"{victory})")
    elif not victory and treasure:
        print(f"{treasure}")


if __name__ == "__main__":
    main()
