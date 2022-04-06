activation_key = input()

while True:
    command = input().split(">>>")

    action = command[0]

    if action == "Generate":
        break

    if action == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        upper_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring = activation_key[start_index:end_index]

        if upper_lower == "Upper":
            substring = "".join(list(map(lambda x: x.upper(), substring)))

        elif upper_lower == "Lower":
            substring = "".join(list(map(lambda x: x.lower(), substring)))

        activation_key = activation_key[:start_index] + substring + activation_key[end_index:]

        print(activation_key)

    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])

        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")