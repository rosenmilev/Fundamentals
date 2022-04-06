def add_item_func(data, item):
    if item not in data:
        data.append(item)

    return data


def removing_item_func(data, item):
    if item in data:
        data.remove(item)

    return data


def combine_items_func(data, item):
    item = item.split(":")
    if item[0] in data:
        data.insert(data.index(item[0]) + 1, item[1])

    return data


def changing_position_func(data, item):
    if item in data:
        data.append(item)
        data.remove(item)

    return data


def command_processing_func(data):

    while True:
        command = input().split(" - ")
        action = command[0]

        if action == "Craft!":
            print(", ".join(data))
            break

        item = command[1]

        if action == "Collect":
            data = add_item_func(data, item)
        elif action == "Drop":
            data = removing_item_func(data, item)
        elif action == "Combine Items":
            data = combine_items_func(data, item)
        elif action == "Renew":
            data = changing_position_func(data, item)


items = input().split(", ")
command_processing_func(items)
