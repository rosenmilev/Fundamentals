import re

text = input()
data = ""

while text != "":
    data += " " + text
    text = input()

pattern = r"www\.[A-Za-z0-9-]+(\.[a-z]+){1,}"

result = re.finditer(pattern, data)

for match in result:
    print(match.group())
