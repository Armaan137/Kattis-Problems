# This problem can be found here: https://open.kattis.com/problems/drinkingsong.

def main():
    n = int(input())
    word = input()

    for i in range(n, 0, -1):
        if i == 1:
            print(f"1 bottle of {word} on the wall, 1 bottle of {word}. Take it down, pass it around, no more bottles of {word}.")
        elif i == 2:
            print(f"2 bottles of {word} on the wall, 2 bottles of {word}. Take one down, pass it around, {i - 1} bottle of {word} on the wall.\n")
        else:
            print(f"{i} bottles of {word} on the wall, {i} bottles of {word}. Take one down, pass it around, {i - 1} bottles of {word} on the wall.\n")


if __name__ == '__main__':
    main()
