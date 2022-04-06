cities = {}

while True:
    city = input().split("||")
    if city[0] == "Sail":
        break

    if city[0] not in cities:
        cities[city[0]] = {}
        cities[city[0]]["population"] = int(city[1])
        cities[city[0]]["gold"] = int(city[2])
    else:
        cities[city[0]]["population"] += int(city[1])
        cities[city[0]]["gold"] += int(city[2])

while True:
    commands = input().split("=>")
    command = commands[0]

    if command == "End":
        break

    town = commands[1]

    if command == "Plunder":
        people_killed = int(commands[2])
        gold_stolen = int(commands[3])

        cities[town]["population"] -= people_killed
        cities[town]["gold"] -= gold_stolen

        print(f"{town} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.")

        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        gold_growth = int(commands[2])

        if gold_growth >= 0:
            cities[town]["gold"] += gold_growth
            print(f"{gold_growth} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")

cities_left = len(cities)

if cities_left > 0:
    print(f"Ahoy, Captain! There are {cities_left} wealthy settlements to go to:")

    for city in cities:
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
