numbers = input().split(", ")

for num in numbers:
    if num == "0":
        numbers.remove("0")
        numbers.append("0")

numbers_list = list(map(int, numbers))
print(numbers_list)
