status_pirate_ship = list(map(int, input().split(">")))
status_warship = list(map(int, input().split(">")))
max_health = int(input())
sunken = False

while True:
    command = input().split()
    action = command[0]

    if action == "Retire":
        print(f"Pirate ship status: {sum(status_pirate_ship)}")
        print(f"Warship status: {sum(status_warship)}")
        break

    if action == "Fire":
        if 0 <= int(command[1]) < len(status_warship):
            status_warship[int(command[1])] -= int(command[2])
            if status_warship[int(command[1])] <= 0:
                print("You won! The enemy ship has sunken.")
                break

    elif action == "Defend":
        if 0 <= int(command[1]) < len(status_pirate_ship) and 0 <= int(command[2]) < len(status_pirate_ship):
            for i in range(int(command[1]), int(command[2]) + 1):
                status_pirate_ship[i] -= int(command[3])
                if status_pirate_ship[i] <= 0:
                    sunken = True
                    break
            if sunken:
                print("You lost! The pirate ship has sunken.")
                break

    elif action == "Repair":
        if 0 <= int(command[1]) < len(status_pirate_ship):
            status_pirate_ship[int(command[1])] += int(command[2])
            if status_pirate_ship[int(command[1])] > max_health:
                status_pirate_ship[int(command[1])] = max_health

    elif action == "Status":
        sections_to_repair = [i for i in status_pirate_ship if i < 0.2 * max_health]
        print(f"{len(sections_to_repair)} sections need repair.")
