import re

pattern = r"\d+"

text = input()
data = ""

while text != "":
    data += " " + text
    text = input()

numbers = re.findall(pattern, data)

print(" ".join(numbers))
