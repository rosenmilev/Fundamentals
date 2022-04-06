def adding_car(cars, current_data):

    current_data = current_data.split("|")
    car = current_data[0]
    mileage = int(current_data[1])
    fuel = int(current_data[2])

    cars[car] = []
    cars[car].append(mileage)
    cars[car].append(fuel)

    return cars


def operations(cars, current_command):
    current_command = current_command.split(" : ")
    action = current_command[0]
    current_car = current_command[1]

    current_mileage = cars[current_car][0]
    current_fuel = cars[current_car][1]

    if action == "Drive":
        distance_to_drive = int(current_command[2])
        fuel_needed = int(current_command[3])

        if current_fuel >= fuel_needed:
            current_mileage += distance_to_drive
            current_fuel -= fuel_needed

            print(f"{current_car} driven for {distance_to_drive} kilometers. {fuel_needed} liters of fuel consumed.")

            if current_mileage >= 100000:
                print(f"Time to sell the {current_car}!")
                cars.pop(current_car)

            else:
                cars[current_car][0] = current_mileage
                cars[current_car][1] = current_fuel

        else:
            print("Not enough fuel to make that ride")

    elif action == "Refuel":
        if current_fuel + int(current_command[2]) > 75:
            cars[current_car][1] = 75
            fuel_filled = 75 - current_fuel
        else:
            fuel_filled = int(current_command[2])
            cars[current_car][1] += fuel_filled

        print(f"{current_car} refueled with {fuel_filled} liters")

    elif action == "Revert":
        kilometers_to_revert = int(current_command[2])

        if current_mileage - kilometers_to_revert < 10000:
            cars[current_car][0] = 10000

        else:
            cars[current_car][0] -= kilometers_to_revert
            print(f"{current_car} mileage decreased by {kilometers_to_revert} kilometers")

    return cars


number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    data = input()
    cars = adding_car(cars, data)

command = input()

while True:

    if command == "Stop":
        break

    cars = operations(cars, command)

    command = input()


for key in cars:
    print(f"{key} -> Mileage: {cars[key][0]} kms, Fuel in the tank: {cars[key][1]} lt.")
