n = int(input())
word = input()

list_of_words = []
list_of_words_containing_word = []

for line in range(n):
    strings = input()
    list_of_words.append(strings)
    if word in strings:
        list_of_words_containing_word.append(strings)

print(list_of_words)
print(list_of_words_containing_word)
