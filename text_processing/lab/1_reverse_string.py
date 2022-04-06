command = input()

while not command == "end":
    reversed_string = command[::-1]

    print(f"{command} = {reversed_string}")

    command = input()
    