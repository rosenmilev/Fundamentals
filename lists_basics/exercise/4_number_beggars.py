offers = input()
number_of_beggars = int(input())

offers = offers.split(", ")
list_of_beggars = []
index = 0

for _ in range(number_of_beggars):
    list_of_beggars.append(0)

for i in range(len(offers)):
    list_of_beggars[index] += int(offers[i])
    index += 1

    if len(list_of_beggars) == index:
        index = 0

print(list_of_beggars)
