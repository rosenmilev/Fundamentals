class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):

        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        info = ""
        if species == "mammal":
            info = f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            info = f"Fishes in {self.name_of_zoo}: {', '.join(self.fish)}\n"
        elif species == "bird":
            info = f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}\n"
        info += f"Total animals: {Zoo.__animals}"
        return info


zoo_name = input()
n = int(input())
zoo = Zoo(zoo_name)

for _ in range(n):
    animal_info = input().split()
    species = animal_info[0]
    name = animal_info[1]
    zoo.add_animal(species, name)

required_species_info = input()

print(zoo.get_info(required_species_info))
