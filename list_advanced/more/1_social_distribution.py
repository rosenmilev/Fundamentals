def distribution(data, minimum):
    wealthiest_person_index = data.index(max(data))
    poorest_person_index = data.index(min(data))

    if 2 * minimum - data[poorest_person_index] <= data[wealthiest_person_index]:
        pass


population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

while True:
    if len(population) * minimum_wealth > sum(population):
        print("No equal distribution possible")
        break

    if len(list(filter(lambda a: a < minimum_wealth, population))) == 0:
        break

