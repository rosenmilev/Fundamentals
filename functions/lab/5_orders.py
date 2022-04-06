def orders(product, quantity):
    if product == "coffee":
        print(f"{1.5 * quantity:.2f}")
    elif product == "water":
        print(f"{1 * quantity:.2f}")
    if product == "coke":
        print(f"{1.4 * quantity:.2f}")
    if product == "snacks":
        print(f"{2 * quantity:.2f}")


curr_product = input()
curr_quantity = int(input())

orders(curr_product, curr_quantity)
