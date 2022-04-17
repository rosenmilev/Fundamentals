items_with_their_prices = input().split("|")
budget = float(input())
train_ticket = 150
money_collected = 0
new_list = []
temp_budget = budget
for item in items_with_their_prices:
    temp_items_with_their_prices = item.split("->")
    temp_type = temp_items_with_their_prices[0]
    temp_price = float(temp_items_with_their_prices[1])

    if "Clothes" in temp_items_with_their_prices:
        if temp_price < 50:
            if temp_budget >= temp_price:
                temp_budget -= temp_price
                money_collected += temp_price * 0.4
                temp_price += temp_price * 0.4
                print(f"{temp_price:.2f}", end=" ")
            else:
                continue
        else:
            continue
    elif "Shoes" in temp_items_with_their_prices:
        if temp_price < 35:
            if temp_budget >= temp_price:
                temp_budget -= temp_price
                money_collected += temp_price * 0.4
                temp_price += temp_price * 0.4
                print(f"{temp_price:.2f}", end=" ")
            else:
                continue
        else:
            continue
    elif "Accessories" in temp_items_with_their_prices:
        if temp_price < 20.50:
            if temp_budget >= temp_price:
                temp_budget -= temp_price
                money_collected += temp_price * 0.4
                temp_price += temp_price * 0.4
                print(f"{temp_price:.2f}", end=" ")
            else:
                continue
        else:
            continue

print(f"\nProfit: {money_collected:.2f}")
if budget + money_collected >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")