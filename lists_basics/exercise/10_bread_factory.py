events_and_products = input().split("|")
energy = 100
coins = 100
flag = True

for command in events_and_products:
    event = command.split("-")
    current_event = event[0]
    current_value = int(event[1])

    if current_event == "rest":
        if current_value + energy <= 100:
            energy += current_value
        else:
            current_value = 0
        print(f"You gained {current_value} energy.")
        print(f"Current energy: {energy}.")

    elif current_event == "order":
        if energy >= 30:
            coins += current_value
            energy -= 30
            print(f"You earned {current_value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= current_value:
            coins -= current_value
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            flag = False
            break

if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
