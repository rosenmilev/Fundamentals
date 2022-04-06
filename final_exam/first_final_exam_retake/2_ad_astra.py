import re

text = input()

pattern = r"(?P<delimiter>(\#|\|))(?P<item_name>[A-Za-z\s]+)(?P=delimiter)" \
          r"(?P<date>\d{2}/\d{2}/\d{2})(?P=delimiter)(?P<calories>\d+)(?P=delimiter)"

matches = re.finditer(pattern, text)

total_calories = 0
foods = []

for match in matches:
    foods.append([f"{match.group('item_name')}", f"{match.group('date')}", f"{match.group('calories')}"])
    total_calories += int(match.group('calories'))

days_to_last = total_calories // 2000

print(f"You have food to last you for: {days_to_last} days!")
[print(f"Item: {curr_food[0]}, Best before: {curr_food[1]}, Nutrition: {curr_food[2]}") for curr_food in foods]
