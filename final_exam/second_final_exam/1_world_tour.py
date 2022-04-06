all_stops = input()


while True:
    command = input().split(":")

    if command[0] == "Travel":
        break

    if command[0] == "Add Stop" and 0 <= int(command[1]) <= len(all_stops) - 1:
        all_stops = all_stops[:int(command[1])] + command[2] + all_stops[int(command[1]):]
        print(all_stops)

    elif command[0] == "Remove Stop" and 0 <= int(command[1]) <= len(all_stops) - 1 and 0 < int(command[2]) <= len(all_stops) - 1:
        all_stops = all_stops[:int(command[1])] + all_stops[int(command[2]) + 1:]
        print(all_stops)

    elif command[0] == "Switch":
        all_stops = all_stops.replace(command[1], command[2])
        print(all_stops)

    else:
        print(all_stops)

print(f"Ready for world tour! Planned stops: {all_stops}")