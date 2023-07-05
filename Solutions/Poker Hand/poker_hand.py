# This problem can be found here: https://open.kattis.com/problems/pokerhand.

def main():
    hand = input().split(" ")

    freq = {}
    for card in hand:
        rank = card[0]
        if rank not in freq:
            freq[rank] = 1
        else:
            freq[rank] += 1

    strength = max(freq.values())

    print(strength)


if __name__ == '__main__':
    main()
