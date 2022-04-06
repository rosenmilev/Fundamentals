courses_information = {}
command = input().split(" : ")

while not command[0] == "end":
    course_name = command[0]
    student_name = command[1]

    if course_name not in courses_information:
        courses_information[course_name] = []
    courses_information[course_name].append(student_name)

    command = input().split(" : ")

for course in courses_information:
    print(f"{course}: {len(courses_information[course])}")
    for student in courses_information[course]:
        print(f"-- {student}")
