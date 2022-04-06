number_of_orders = int(input())

total_price = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    price = days * price_per_capsule * capsules_count
    total_price += price

    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
