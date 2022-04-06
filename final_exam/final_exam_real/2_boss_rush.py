import re

number_of_inputs = int(input())

pattern = r"\|[A-Z]{4,}\|\:\#[A-Za-z]+\s[A-Za-z]+\#"

for _ in range(number_of_inputs):
    current_input = input()
    result = re.findall(pattern, current_input)

    if result:
        current_boss = result[0].split(":")
        name = current_boss[0][1:len(current_boss[0]) - 1]
        title = current_boss[1][1:len(current_boss[1]) - 1]

        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")

    else:
        print("Access denied!")
