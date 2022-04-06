initial_loot = input().split("|")
length = 0

while True:
    command = input().split(" ")
    action = command[0]
    if action == "Yohoho!":
        break
    if action == "Loot":
        for item in range(1, len(command)):
            if command[item] not in initial_loot:
                initial_loot.insert(0, command[item])
    elif action == "Drop":
        if 0 <= int(command[1]) < len(initial_loot):
            initial_loot.append(initial_loot.pop(int(command[1])))
    elif action == "Steal":
        if len(initial_loot) > int(command[1]):
            stolen_items = initial_loot[len(initial_loot) - int(command[1]):]
            print(", ".join(stolen_items))
            initial_loot = initial_loot[:len(initial_loot) - int(command[1])]
        else:
            print(", ".join(initial_loot))
            initial_loot = []

if len(initial_loot) > 0:
    for i in initial_loot:
        length += len(i)
    aver_treasure_gain = length / len(initial_loot)
    print(f"Average treasure gain: {aver_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
