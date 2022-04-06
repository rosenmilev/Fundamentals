def operations(current_message, current_command):

    current_command = current_command.split(":|:")

    action = current_command[0]

    if action == "InsertSpace":
        i = int(current_command[1])

        current_message = current_message[:i] + " " + current_message[i:]

        print(current_message)

    elif action == "Reverse":
        substring = current_command[1]

        if substring in current_message:
            current_message = current_message.replace(substring, "", 1)
            reversed_substring = substring[::-1]

            current_message += reversed_substring
            print(current_message)

        else:
            print("error")

    elif action == "ChangeAll":

        substring = current_command[1]
        replacement = current_command[2]

        current_message = current_message.replace(substring, replacement)

        print(current_message)

    return current_message


message = input()
command = input()

while True:

    if command == "Reveal":
        print(f"You have a new text message: {message}")

        break

    message = operations(message, command)

    command = input()
