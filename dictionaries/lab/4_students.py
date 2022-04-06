courses = {}
while True:
    data = input().split(":")

    if len(data) == 1:
        break

    if data[2] not in courses:
        courses[data[2]] = {}

    courses[data[2]][data[1]] = data[0]

searched_course = " ".join((" ".join(data)).split("_"))

for course in courses:
    if searched_course == course:
        for id, name in courses[searched_course].items():
            print(f"{name} - {id}")
