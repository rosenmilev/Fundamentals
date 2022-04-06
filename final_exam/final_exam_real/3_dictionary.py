def adding_words(dictionary, data):
    data = data.split(": ")
    word = data[0]
    definition = data[1]

    if word not in dictionary:
        dictionary[word] = []
        dictionary[word].append(definition)
    else:
        dictionary[word].append(definition)

    return dictionary


dictionary = {}

all_words = input().split(" | ")

for word in all_words:
    dictionary = adding_words(dictionary, word)

testing_words = input().split(" | ")

command = input()

if command == "Test":
    for current_word_to_find in testing_words:
        if current_word_to_find in dictionary:

            print(f"{current_word_to_find}:")

            for definition in dictionary[current_word_to_find]:

                print(f"-{definition}")

elif command == "Hand Over":
    words = [key for key in dictionary]
    [print(words[i]) if i == len(words) - 1 else print(words[i] + " ", end="") for i in range(len(words))]
