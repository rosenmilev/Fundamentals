third = input()
second = input()
first = input()

list_of_animals = [third, second, first]

list_of_animals[0], list_of_animals[2] = list_of_animals[2], list_of_animals[0]

print(list_of_animals)