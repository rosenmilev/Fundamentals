countries = input().split(", ")
capitals = input().split(", ")

result = dict(zip(countries, capitals))

for country, city in result.items():
    print(f"{country} -> {city}")