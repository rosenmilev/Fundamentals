collection_of_items = input()
budget = float(input())

collection_of_items = collection_of_items.split("|")
profit = 0
turnover = 0

for item in collection_of_items:
    current_item = item.split("->")
    current_item_name = current_item[0]
    current_item_price = float(current_item[1])

    if budget - current_item_price < 0:
        continue

    if current_item_name == "Clothes":
        if current_item_price <= 50:
            current_item_selling_price = current_item_price * 1.4
            print(f"{current_item_selling_price:.2f}", end=" ")
            budget -= current_item_price
            profit += current_item_price * 0.4
            turnover += current_item_selling_price
        else:
            continue
    elif current_item_name == "Shoes":
        if current_item_price <= 35:
            current_item_selling_price = current_item_price * 1.4
            print(f"{current_item_selling_price:.2f}", end=" ")
            budget -= current_item_price
            profit += current_item_price * 0.4
            turnover += current_item_selling_price
        else:
            continue
    elif current_item_name == "Accessories":
        if current_item_price <= 20.50:
            current_item_selling_price = current_item_price * 1.4
            print(f"{current_item_selling_price:.2f}", end=" ")
            budget -= current_item_price
            profit += current_item_price * 0.4
            turnover += current_item_selling_price
        else:
            continue

print(f"\nProfit: {profit:.2f}")
if (turnover + budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
