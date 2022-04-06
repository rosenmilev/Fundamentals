number_of_rooms = int(input())
total_free_chairs = 0
all_visitors_accommodated = True

for room in range(1, number_of_rooms + 1):
    chair_visitors_info = input().split(" ")
    free_chairs = len(chair_visitors_info[0])
    number_of_visitors = int(chair_visitors_info[1])

    if number_of_visitors > free_chairs:
        print(f"{number_of_visitors - free_chairs} more chairs needed in room {room}")
        all_visitors_accommodated = False
    else:
        total_free_chairs += free_chairs - number_of_visitors

if all_visitors_accommodated:
    print(f"Game On, {total_free_chairs} free chairs left")
