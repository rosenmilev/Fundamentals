def search(searched_name):
    if searched_name in phones:
        print(f"{searched_name} -> {phones[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")


phones = {}
data = input()

while "-" in data:
    data = data.split("-")
    name = data[0]
    number = data[1]

    phones[name] = number

    data = input()

n = int(data)

for _ in range(n):
    search(searched_name=input())
