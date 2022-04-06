# quantities = {}
#
# while True:
#     kvp = input().split(": ")
#
#     if kvp[0] == "statistics":
#         break
#
#     key = kvp[0]
#     value = int(kvp[1])
#
#     if key in quantities:
#         quantities[key] += value
#     else:
#         quantities[key] = value
#
# print("Products in stock:")
# for quant in quantities:
#     print(f"- {quant}: {quantities[quant]}")
# print(f"Total Products: {len(quantities.keys())}")
# print(f"Total Quantity: {sum(quantities.values())}")
# SECOND WAY

kvp = input()
products = {}

while not kvp == "statistics":
    key, value = kvp.split(": ")

    if key not in products:
        products[key] = int(value)
    else:
        products[key] += int(value)

    kvp = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")