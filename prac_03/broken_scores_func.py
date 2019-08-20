def main():
    determine_score()


def determine_score():
    score = float(input("Enter Score: "))
    if 90 <= score <= 100:
        print("Excellent")
    elif 90 > score >= 50:
        print("Passable")
    elif 50 > score > 0:
        print("Bad")
    else:
        print("invalid score")


main()
