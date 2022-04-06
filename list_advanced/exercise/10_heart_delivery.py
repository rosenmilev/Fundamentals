
neighborhood = list(map(int, input().split("@")))
current_index = 0

while True:
    command = input().split()

    if command[0] == "Love!":
        print(f"Cupid's last position was {current_index}.")
        if len([i for i in neighborhood if not i == 0]) > 0:
            print(f"Cupid has failed {len([i for i in neighborhood if not i == 0])} places.")
        else:
            print("Mission was successful.")
        break
    jump_length = int(command[1])
    current_index += jump_length

    if current_index <= len(neighborhood) - 1:
        if neighborhood[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighborhood[current_index] -= 2
            if neighborhood[current_index] <= 0:
                print(f"Place {current_index} has Valentine's day.")
                neighborhood[current_index] = 0
    else:
        current_index = 0
        if neighborhood[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            neighborhood[current_index] -= 2
            if neighborhood[current_index] <= 0:
                print(f"Place {current_index} has Valentine's day.")
                neighborhood[current_index] = 0
