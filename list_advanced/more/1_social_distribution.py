def distribution(data, minimum):

    for i in range(len(data)):
        wealthiest_person_index = data.index(max(data))
        poorest_person_index = data.index(min(data))

        if len(list(filter(lambda a: a < minimum_wealth, population))) == 0:
            break

        if data[i] < minimum:
            data[wealthiest_person_index] -= minimum - data[i]
            data[i] = minimum

    return data


population = list(map(int, input().split(", ")))
minimum_wealth = int(input())


if len(population) * minimum_wealth > sum(population):
    print("No equal distribution possible")
else:
    print(distribution(population, minimum_wealth))
