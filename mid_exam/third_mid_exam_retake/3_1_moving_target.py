def target_command(input_data: list, action, index, value):
    removing_input_data = input_data.copy()
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
        if index >= len(input_data) or (index + value) >= len(input_data) or value + 1 > index:
            print("Strike missed!")
        else:
            for i in range(index - value, index + value + 1):
                input_data.remove(removing_input_data[i])
    elif action == "End":
        print("|".join(list(map(str, input_data))))


curr_targets = input().split()
curr_command = [0]
curr_targets = list(map(int, curr_targets))

while True:
    curr_command = input().split()
    if curr_command[0] == "End":
        break
    curr_index = int(curr_command[1])
    curr_value = int(curr_command[2])
    curr_action = curr_command[0]
    target_command(curr_targets, curr_action, curr_index, curr_value)


