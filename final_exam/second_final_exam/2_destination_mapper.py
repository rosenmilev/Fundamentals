import re

text = input()

pattern = r"(\=|\/)[A-Z][A-Za-z]{2,}(\1)"

result = re.finditer(pattern, text)

destinations = []
points = 0

for res in result:
    current_destination = res.group()[1:len(res.group()) - 1]
    destinations.append(current_destination)
    points += int(len(current_destination))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
