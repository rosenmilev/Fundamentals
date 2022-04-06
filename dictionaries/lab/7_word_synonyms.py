synonyms_dict = {}
n = int(input()) * 2

words = [input() for _ in range(n)]

for i in range(0, n, 2):
    if words[i] not in synonyms_dict and i % 2 == 0:
        synonyms_dict[words[i]] = []
    synonyms_dict[words[i]].append(words[i + 1])

for key in synonyms_dict:
    print(f"{key} - {', '.join(synonyms_dict[key])}")
