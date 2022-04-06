words = input().split(" ")
word_dict = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in word_dict:
        word_dict[word_lower] = 0
    word_dict[word_lower] += 1

for key in word_dict:
    if word_dict[key] % 2 == 1:
        print(key, end=" ")
