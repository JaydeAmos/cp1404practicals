out_file = open("name.txt", "w")
user_name = input("Enter your name: ")
print(user_name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
user_name = in_file.read().strip()
in_file.close()
print("Your name is", user_name)

with open("name.txt", "r") as in_file:
    user_name = in_file.read().strip()
print("You name is", user_name)

in_file = open("numbers.txt", "r")
num_one = int(in_file.readline())
num_two = int(in_file.readline())
in_file.close()
print(num_one + num_two)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
