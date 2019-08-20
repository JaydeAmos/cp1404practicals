MIN_LENGTH = 5


def main():
    get_password()


def get_password():
    password = input("Enter password of at least 5 characters: ")
    while len(password) < MIN_LENGTH:
        password = input("Enter password of at least 5 characters: ")
    print("Your password is", '*' * len(password))


main()
