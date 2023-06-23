# This problem can be found here: https://open.kattis.com/problems/bubbletea.

def main():
    num_teas = int(input())
    tea_prices = list(map(int, input().split()))

    num_toppings = int(input())
    topping_prices = list(map(int, input().split()))

    valid_toppings = {}
    for i in range(num_teas):
        toppings = list(map(int, input().split()))
        valid_toppings[i + 1] = toppings[1:]

    money = int(input())

    max_students = 0
    for i in range(num_teas):
        for j in valid_toppings[i + 1]:
            print(j, j-1, topping_prices)
            cost = tea_prices[i] + topping_prices[j - 1]
            if cost <= money:
                max_students = max(max_students, money // cost)

    students = max_students - 1

    if students > 0:
        print(students)
    else:
        print(0)


if __name__ == "__main__":
    main()
