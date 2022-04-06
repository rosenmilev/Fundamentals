n = int(input())

numbers = []
matched_numbers = []

for _ in range(n):
    current_integer = int(input())
    numbers.append(current_integer)
command = input()

for current_integer in numbers:
    if command == "even" and current_integer % 2 == 0:
        matched_numbers.append(current_integer)
    elif command == "odd" and current_integer % 2 == 1:
        matched_numbers.append(current_integer)
    elif command == "negative" and current_integer < 0:
        matched_numbers.append(current_integer)
    elif command == "positive" and current_integer >= 0:
        matched_numbers.append(current_integer)

print(matched_numbers)

