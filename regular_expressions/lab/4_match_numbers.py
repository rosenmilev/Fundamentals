import re

text = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, text)

result = [match.group() for match in matches]

print(*result)

