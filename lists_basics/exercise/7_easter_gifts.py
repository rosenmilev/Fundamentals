gifts_to_buy = input()
gifts_to_buy = gifts_to_buy.split()

while True:
    command = input()
    if command == "No Money":
        break

    command = command.split()
    if command[0] == "OutOfStock":
        for i in range(len(gifts_to_buy)):
            if str(gifts_to_buy[i]) == str(command[1]):
                gifts_to_buy[i] = "None"

    elif command[0] == "Required":
        if len(gifts_to_buy) > int(command[2]) > 0:
            gifts_to_buy[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts_to_buy[len(gifts_to_buy) - 1] = command[1]

for gift in gifts_to_buy:
    if not gift == "None":
        print(gift, end=" ")
