import random

LINE_NUMBERS = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    user_quick_pick_total = int(input("How many quick picks? "))
    while user_quick_pick_total < 0:
        print("Invalid Input")
        user_quick_pick_total = int(input("How many quick picks? "))

    for i in range(user_quick_pick_total):
        quick_pick = []
        for j in range(LINE_NUMBERS):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
