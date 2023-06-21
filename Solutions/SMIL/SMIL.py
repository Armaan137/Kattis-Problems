# The problem can be found here: https://open.kattis.com/problems/smil.

def main():
    line = [line for line in input()]
    for i, letter in enumerate(line):
        if letter == ':' or letter == ';':
            if i < len(line) - 1 and line[i + 1] == ')':
                print(i)
            elif i < len(line) - 2 and line[i + 1] == '-' and line[i + 2] == ')':
                print(i)


if __name__ == "__main__":
    main()
