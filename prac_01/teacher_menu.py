num_one = int(input("Enter first number: "))
num_two = int(input("Enter first number: "))
choice = input("What would you like to do with these numbers?\n(E)ven numbers only\n(O)dd numbers only\n"
               "(S)quare the numbers\n(Q)uit").upper()
while choice != "Q":
    if choice == "E":
        print()
    elif choice == "O":
        print("oddnumber")
    elif choice == "S":
        print("both numbers squared")
    else:
        print("Invalid Choice")
    choice = input("What would you like to do with these numbers?\n(E)ven numbers only\n(O)dd numbers only\n"
                   "(S)quare the numbers\n(Q)uit").upper()
print("END")