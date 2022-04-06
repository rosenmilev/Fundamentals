numbers = list(map(int, input().split(", ")))
current_tens = 10

while True:
    group_of_current_tens = [i for i in numbers if i <= current_tens]
    print(f"Group of {current_tens}'s: {group_of_current_tens}")
    [numbers.remove(i) for i in group_of_current_tens]
    current_tens += 10
    if len(numbers) == 0:
        break
