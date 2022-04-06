products = {}

while True:
    command = input().split(" ")

    if command[0] == "buy":
        break

    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in products:
        products[product] = [price, quantity]

    else:
        products[product][0] = price
        products[product][1] += quantity

for prod, atributes in products.items():
    total_price = atributes[0] * atributes[1]
    print(f"{prod} -> {total_price:.2f}")
