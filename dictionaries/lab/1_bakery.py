# elements = input().split(" ")

# keys = []
# values = []
#
# for i in range(len(elements)):
#     if i % 2 == 0:
#         keys.append(elements[i])
#     else:
#         values.append(int(elements[i]))
#
# table_of_contents = zip(keys, values)
#
# print(dict(table_of_contents))
# SECOND WAY

# elements = input().split(" ")
#
# keys = [elements[i] for i in range(0, len(elements), 2)]
# values = [int(elements[i]) for i in range(1, len(elements), 2)]
#
# table_of_contents = dict(zip(keys, values))
#
# print(table_of_contents)
# THIRD WAY

elements = input().split(" ")
products = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = elements[index + 1]
    products[key] = int(value)

print(products)
