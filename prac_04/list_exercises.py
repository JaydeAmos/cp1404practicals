numbers = []

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("the first number is", numbers[0])
print("the last number is", numbers[-1])
print("the smallest number is", min(numbers))
print("the largest number is", max(numbers))
print("the average of the nunmbers is", sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
users_name = input("Enter username: ")
if users_name in usernames:
    print("Access granted")
else:
    print("Access denied")
