data = input()

while True:
    command = input().split(" ")
    action = command[0]

    if action == "End":
        break

    if action == "Translate":
        char = command[1]
        replacement = command[2]

        data = data.replace(char, replacement)
        print(data)

    elif action == "Includes":
        substring = command[1]

        if substring in data:
            print(True)
        else:
            print(False)

    elif action == "Start":
        substring = command[1]

        if data.find(substring) == 0:
            print(True)
        else:
            print(False)

    elif action == "Lowercase":

        data = data.lower()
        print(data)

    elif action == "FindIndex":
        char = command[1]
        last_occurrence = len(data) - data[::-1].find(char) - 1

        print(last_occurrence)

    elif action == "Remove":
        starting_index = int(command[1])
        count = int(command[2])
        ending_index = starting_index + count

        data = data[:starting_index] + data[ending_index:]
        print(data)
