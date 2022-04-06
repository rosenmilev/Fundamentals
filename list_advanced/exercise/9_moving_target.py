targets = list(map(int, input().split()))

while True:
    command = input().split()
    action = command[0]

    if action == "End":
        print("|".join(list(map(str, targets))))
        break

    current_index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        if 0 <= current_index <= len(targets) - 1:
            targets[current_index] -= value
            if targets[current_index] <= 0:
                targets.pop(current_index)

    elif action == "Add":
        if 0 <= current_index <= len(targets) - 1:
            targets.insert(current_index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if 0 <= current_index - value and current_index + value <= len(targets) - 1:
            for i in range(current_index - value, current_index + value + 1):
                targets.pop(current_index - value)
        else:
            print("Strike missed!")
