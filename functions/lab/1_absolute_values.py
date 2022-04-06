input_numbers = input().split()
input_numbers = list(map(float, input_numbers))

for num in range(len(input_numbers)):
    if input_numbers[num] < 0:
        input_numbers[num] = abs(input_numbers[num])

print(input_numbers)