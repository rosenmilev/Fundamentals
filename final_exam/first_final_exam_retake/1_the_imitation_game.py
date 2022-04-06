message = input()


while True:
    command = input().split("|")

    if command[0] == "Decode":
        break

    if command[0] == "Move":
        message = message[int(command[1]):] + message[:int(command[1])]

    elif command[0] == "Insert":
        message = message[:int(command[1])] + command[2] + message[int(command[1]):]

    elif command[0] == "ChangeAll":
        message = message.replace(command[1], command[2])

print(f"The decrypted message is: {message}")
