numbers = list(map(int, input().split()))

while True:
    command = input().split()
    action = command[0]

    if action == "Finish":
        numbers = list(map(str, numbers))
        print(" ".join(numbers))
        break

    value = int(command[1])

    if action == "Add":
        numbers.append(value)

    elif action == "Remove":
        if value in numbers:
            numbers.remove(value)

    elif action == "Replace":
        replacement = int(command[2])
        if value in numbers:
            numbers[numbers.index(value)] = replacement

    elif action == "Collapse":
        numbers = [num for num in numbers if num >= value]
