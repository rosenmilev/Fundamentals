budget = float(input())
price_of_flour = float(input())

egg_price = 0.75 * price_of_flour
price_of_milk_per_liter = 1.25 * price_of_flour

price_of_one_loaves = egg_price + price_of_flour + 0.25 * price_of_milk_per_liter

number_of_loaves = 0
colored_eggs = 0

while True:
    if budget < price_of_one_loaves:
        break
    budget = budget - price_of_one_loaves
    number_of_loaves += 1
    if number_of_loaves % 3 == 0:
        colored_eggs += 3 - (number_of_loaves - 2)
    else:
        colored_eggs += 3

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")