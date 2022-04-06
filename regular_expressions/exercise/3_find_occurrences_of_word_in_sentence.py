import re

text_to_search = input()
searched_word = input()

pattern = rf"\b{searched_word}\b"

result = re.findall(pattern, text_to_search, re.IGNORECASE)

print(len(result))
