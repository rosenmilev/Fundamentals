collection_of_items = input()
budget = float(input())
collection_of_items = collection_of_items.split("|")

bought_items = []
profit = 0
turnover = 0
list_of_items = ["Clothes", "Shoes", "Accessories"]

for item in collection_of_items:
    current_item = item.split("->")
    current_item_name = current_item[0]
    current_item_price = float(current_item[1])

    if current_item_name not in list_of_items:
        continue
    if current_item_price > budget:
        continue
    if current_item_name not in list_of_items:
        continue
    if current_item_name == "Clothes" and current_item_price > 50:
        continue
    if current_item_name == "Shoes" and current_item_price > 35:
        continue
    if current_item_name == "Accessories" and current_item_price > 20.50:
        continue

    budget -= current_item_price
    selling_price = current_item_price * 1.4
    turnover += selling_price
    profit += current_item_price * 0.4
    selling_price = "{:.2f}".format(selling_price)
    bought_items.append(selling_price)

for el in bought_items:
    print(el, end=" ")

print(f"\nProfit: {profit:.2f}")
if (turnover + budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
