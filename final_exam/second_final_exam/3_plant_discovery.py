number_of_plants = int(input())
plants = {}

for _ in range(number_of_plants):
    current_plant = input().split("<->")
    if current_plant[0] not in plants:
        plants[current_plant[0]] = []
        plants[current_plant[0]].append(current_plant[1])
        plants[current_plant[0]].append(0)
    else:
        plants[current_plant[0]] = current_plant[1]

while True:
    command = input().split(": ")

    if command[0] == "Exhibition":
        break

    operation = command[0]
    data = command[1].split(" - ")

    if data[0] not in plants:
        print("error")
        continue

    if operation == "Rate":
        plants[data[0]].append(int(data[1]))

    elif operation == "Update":
        plants[data[0]][0] = data[1]

    elif operation == "Reset":
        rarity = plants[data[0]][0]
        plants[data[0]].clear()
        plants[data[0]].append(rarity)
        plants[data[0]].append(0)

for key in plants:
    if len(plants[key]) > 2:
        plants[key][1] = sum(plants[key][1:]) / len(plants[key][2:])

print("Plants for the exhibition:")

for key, value in plants.items():
    print(f"- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}")
