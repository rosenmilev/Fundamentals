number_of_commands = int(input())
registered_vehicles = {}

for _ in range(number_of_commands):
    current_user_data = input().split(" ")
    command = current_user_data[0]
    username = current_user_data[1]

    if command == "register":
        license_plate_number = current_user_data[2]

        if username not in registered_vehicles:
            registered_vehicles[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif command == "unregister":
        if username not in registered_vehicles:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            registered_vehicles.pop(username)

for user, license_plate in registered_vehicles.items():
    print(f"{user} => {license_plate}")
