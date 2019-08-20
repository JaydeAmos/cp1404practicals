user_name = input("What is your name?").upper()
menu_choice = input("(H)ello\n(G)oodbye\n(Q)uit").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello", user_name)
    elif menu_choice == "G":
        print("Goodbye", user_name)
    else:
        print("Invalid message")
    menu_choice = input("(H)ello\n(G)oodbye\n(Q)uit").upper()
print("END")


