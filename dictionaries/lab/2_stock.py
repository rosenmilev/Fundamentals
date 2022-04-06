products = input().split(" ")

quantities = {}

for index in range(0, len(products), 2):
    quantities[products[index]] = products[index + 1]

products_to_search = input().split(" ")

for product in products_to_search:
    if product in quantities:
        print(f"We have {quantities[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
