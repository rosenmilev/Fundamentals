neighbourhood = input().split("@")
neighbourhood = list(map(int, neighbourhood))
position = 0

while True:
    command = input().split()
    action = command[0]

    if action == "Love!":
        print(f"Cupid's last position was {position}.")
        failed_house_count = len([i for i in neighbourhood if i > 0])
        if failed_house_count == 0:
            print("Mission was successful.")
        else:
            print(f"Cupid has failed {failed_house_count} places.")
        break

    length = int(command[1])

    if action == "Jump":
        if position + length > len(neighbourhood) - 1:
            position = 0
        else:
            position += length

        if neighbourhood[position] > 0:
            neighbourhood[position] -= 2
            if neighbourhood[position] <= 0:
                print(f"Place {position} has Valentine's day.")
        else:
            print(f"Place {position} already had Valentine's day.")
