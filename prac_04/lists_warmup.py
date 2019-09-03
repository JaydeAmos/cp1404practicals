# numbers[0] - 3
# numbers[-1] - 2
# numbers[3] - 1
# numbers[:-1] - 3, 1, 4, 1, 5, 9
# numbers[3:4] - 1
# 5 in numbers - code had no effect
# 7 in numbers - code had no effect
# "3" in numbers - code had no effect
# numbers + [6, 5, 3]

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)

numbers[0] = "ten"
print(numbers)

numbers[-1] = 1
print(numbers)

numbers[2:]
print(numbers)

9 in numbers
