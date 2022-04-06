string_of_animals = input()
string_of_animals = string_of_animals.split(", ")

if string_of_animals[len(string_of_animals) - 1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(string_of_animals)):
        if string_of_animals[i] == "wolf":
            print(f"Oi! Sheep number {len(string_of_animals) - 1 - i}! You are about to be eaten by a wolf!")
