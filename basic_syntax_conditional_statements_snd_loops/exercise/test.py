budget = float(input())
price_of_flour = float(input())

numbers_of_colored_eggs = 0

price_of_eggs = price_of_flour * 0.75
price_of_milk = price_of_flour * 1.25

price_of_bread = price_of_flour + price_of_eggs + 0.25 * price_of_milk
number_of_bread = int(budget // price_of_bread)
money_left = budget - number_of_bread * price_of_bread

current_number_of_bread = number_of_bread

for i in range(1, number_of_bread + 1):#
    numbers_of_colored_eggs += 3#
    if i % 3 == 0:
        numbers_of_colored_eggs -= (i - 2)

print(f"You made {int(number_of_bread)} loaves of Easter bread! Now you have {int(numbers_of_colored_eggs)} eggs and "
      f"{money_left:.2f}BGN left.")