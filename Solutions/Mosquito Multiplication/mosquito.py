# This problem can be found here: https://open.kattis.com/problems/mosquito.

def main():
    while True:
        try:
            line = input()
        except EOFError:
            break

        mosquitoes, pupae, larvae, e, r, s, n = map(int, line.split(" "))

        for _ in range(n):
            num_larvae = mosquitoes * e
            num_pupae = larvae // r
            num_adults = pupae // s
            larvae = num_larvae
            pupae = num_pupae
            mosquitoes = num_adults

        print(mosquitoes)


if __name__ == '__main__':
    main()
