items_collected = {}
key_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
condition = False

while True:
    data = input().lower()
    data = data.split()

    for i in range(1, len(data), 2):

        if data[i].lower() not in items_collected:
            items_collected[data[i].lower()] = int(data[i - 1])
        else:
            items_collected[data[i].lower()] += int(data[i - 1])

        if data[i].lower() in key_items:
            if items_collected[data[i].lower()] >= 250:
                print(f"{key_items[data[i].lower()]} obtained!")
                items_collected[data[i].lower()] -= 250
                condition = True

        if condition:
            break
    if condition:
        break

for item in key_items.keys():
    if item in items_collected:
        print(f"{item}: {items_collected[item]}")
        del items_collected[item]
    else:
        print(f"{item}: 0")

for junk, quantity in items_collected.items():
    print(f"{junk}: {quantity}")
