import re

text = input()

pattern = r"(\:|\*)\1[A-Z][a-z]{2,}\1\1"
pattern_two = r"\d"

emojis = re.finditer(pattern, text)
numbers = re.findall(pattern_two, text)

cool_threshold = int(numbers[0])
all_emojis = {}

for i in range(1, len(numbers)):
    cool_threshold *= int(numbers[i])

print(f"Cool threshold: {cool_threshold}")

for emoji in emojis:
    current_emoji = emoji.group()[2:len(emoji.group()) - 2]
    all_emojis[emoji.group()] = sum([ord(i) for i in current_emoji])

print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
[print(key) for key, value in all_emojis.items() if value >= cool_threshold]
