price = 0
taxes = 0
discount = 0

while True:
    current_price = input()

    if current_price == "special":
        taxes = 0.2 * price
        discount = (price + taxes) * 0.1
        break
    elif current_price == "regular":
        taxes = 0.2 * price
        break

    current_price = float(current_price)

    if current_price < 0:
        print("Invalid price!")
    else:
        price += current_price

if price > 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price + taxes - discount:.2f}$")
else:
    print("Invalid order!")
