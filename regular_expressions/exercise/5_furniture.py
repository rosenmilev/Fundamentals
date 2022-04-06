import re

command = input()
total_commands = ""
pattern = r"(^|(?<=\s))>>(?P<name>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)($|(?=\s))"
total_sum = 0


while not command == "Purchase":
    total_commands += " " + command
    command = input()

valid_commands = re.finditer(pattern, total_commands)

print("Bought furniture:")

for group in valid_commands:
    current_name = group.group("name")
    current_price = group.group("price")
    current_quantity = group.group("quantity")
    total_sum += float(current_price) * int(current_quantity)
    print(current_name)

print(f"Total money spend: {total_sum:.2f}")
