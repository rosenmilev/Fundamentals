def operations(current_password, current_command):
    current_command = current_command.split(" ")
    new_password = ""
    action = current_command[0]

    if action == "TakeOdd":
        for i in range(1, len(current_password), 2):
            new_password += current_password[i]
        print(new_password)

    elif action == "Cut":
        i = int(current_command[1])
        length = int(current_command[2])
        substring = current_password[i:i + length]
        new_password = current_password.replace(substring, "", 1)
        print(new_password)

    elif action == "Substitute":
        substring = current_command[1]
        replacement = current_command[2]

        if substring in current_password:
            new_password = current_password.replace(substring, replacement)
            print(new_password)
        else:
            new_password = current_password
            print("Nothing to replace!")

    return new_password


password = input()
command = input()

while True:
    if command == "Done":
        print(f"Your password is: {password}")
        break
    password = operations(password, command)

    command = input()
