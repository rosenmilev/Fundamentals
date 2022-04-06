factor = int(input())
elements_count = int(input())

list_of_multiplies = []
element = factor

for _ in range(elements_count):
    if element > 0:
        list_of_multiplies.append(element)
    element += factor

print(list_of_multiplies)
