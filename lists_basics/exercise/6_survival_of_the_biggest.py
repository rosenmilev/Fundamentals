numbers = input()
count_to_remove = int(input())

numbers = numbers.split()
numbers_sorted = []

for el in numbers:
    numbers_sorted.append(int(el))

numbers_sorted = sorted(numbers_sorted)

for i in range(count_to_remove):
    numbers.remove(str(numbers_sorted[i]))

print(", ".join(numbers))
