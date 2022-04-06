input_data = input().split()

input_data = list(map(int, input_data))

while True:
    command = input().split()
    removing_input_data = input_data.copy()

    if command[0] == "End":
        print("|".join(list(map(str, input_data))))
        break

    index = int(command[1])
    value = int(command[2])
    action = command[0]

    if action == "Shoot":
        if index < len(input_data):
            input_data[index] -= value
            if input_data[index] <= 0:
                input_data.pop(index)

    elif action == "Add":
        if index >= len(input_data):
            print("Invalid placement!")
        else:
            input_data.insert(index, value)

    elif action == "Strike":
        if index >= len(input_data) or (index + value) >= len(input_data) or value > index:
            print("Strike missed!")
        else:
            for i in range(index - value, index + value + 1):
                input_data.pop(index - value)
