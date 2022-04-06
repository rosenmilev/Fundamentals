def count_submissions(statistics_dict: dict, course: str):

    more_than_one_submissions = 0

    for value in statistics_dict[course].values():
        if len(value) > 1:
            more_than_one_submissions += len(value) - 1

    return more_than_one_submissions + len(statistics_dict[course])


command = input().split("-")

statistics_dict = {}
banned_students = []

while not command[0] == "exam finished":
    username = command[0]

    if command[1] == "banned" and username not in banned_students:
        banned_students.append(username)

    else:
        language = command[1]
        points = int(command[2])

        if language not in statistics_dict:
            statistics_dict[language] = {}

        if username not in statistics_dict[language]:
            statistics_dict[language][username] = []

        statistics_dict[language][username].append(points)

    command = input().split("-")

print("Results:")

for course, submissions in statistics_dict.items():
    for student, result in submissions.items():
        if student not in banned_students:
            print(f"{student} | {max(result)}")

print("Submissions:")

for course in statistics_dict:
    print(f"{course} - {count_submissions(statistics_dict, course)}")
