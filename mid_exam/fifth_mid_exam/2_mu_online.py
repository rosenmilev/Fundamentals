rooms = input().split("|")
initial_health = 100
bitcoins = 0
current_number = 0
alive = True

for current_room in rooms:
    current_room = current_room.split(" ")
    command = current_room[0]
    number = int(current_room[1])
    current_number += 1
    if command == "potion":
        if initial_health + number <= 100:
            initial_health += number
            print(f"You healed for {number} hp.")
        else:
            print(f"You healed for {100 - initial_health} hp.")
            initial_health = 100
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {current_number}")
            alive = False
            break

if alive:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")



