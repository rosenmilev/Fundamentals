shopping_list = input().split("!")

while True:
    command = input().split()
    action = command[0]

    if action == "Go":
        print(", ".join(shopping_list))
        break

    item = command[1]

    if action == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif action == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
    elif action == "Correct":
        if item in shopping_list:
            shopping_list[shopping_list.index(item)] = command[2]
    elif action == "Rearrange":
        if item in shopping_list:
            shopping_list.append(item)
            shopping_list.remove(item)
