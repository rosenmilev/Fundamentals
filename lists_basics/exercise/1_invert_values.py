string_of_numbers = input()

list_of_numbers = string_of_numbers.split()
list_of_numbers: list
index = 0

for num in list_of_numbers:
    num = -int(num)
    list_of_numbers[index] = num
    index += 1

print(list_of_numbers)
