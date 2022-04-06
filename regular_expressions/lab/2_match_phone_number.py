import re

number = input()

regex = r"\+359([\s-])2(\1)\d{3}(\1)\d{4}"

matches = re.finditer(regex, number)

valid_phones = [x.group() for x in matches]

print(", ".join(valid_phones))
