total = 0
number_of_items = int(input("Please enter how many items you have: "))
while number_of_items <= 0:
    print("You have no items")
    number_of_items = int(input("Please enter how many items you have: "))

for i in range(number_of_items):
    item_price = float(input("Price of Item: "))
    total += item_price

if total > 100:
    total *= 0.9

print("The total price for ", number_of_items, " items is $", total, sep='')

print("The total price for {} items is ${:.2f}".format(number_of_items, total))
