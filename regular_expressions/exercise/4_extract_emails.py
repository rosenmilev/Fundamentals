import re

text = input()

pattern = r"(^|(?<=\s))\b[A-Za-z0-9]+([-._][A-Za-z0-9]+\b)?@\b[A-Za-z]+-?[A-Za-z]+(\.\b[A-Za-z]+(-?[A-Za-z]+\b)?){1,}"

result = re.finditer(pattern, text)

[print(match.group()) for match in result]
