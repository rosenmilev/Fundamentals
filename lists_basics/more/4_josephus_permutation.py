people_in_circle = input().split()
k = int(input())

current_executed_people = []
executed_people = []
counter = 0

while people_in_circle:

    for i in range(len(people_in_circle)):
        counter += 1
        if counter % k == 0:
            current_executed_people.append(people_in_circle[i])

    for people in current_executed_people:
        executed_people.append(people)
        people_in_circle.remove(people)

    current_executed_people.clear()

result = ",".join(executed_people)

# while True:
#     if counter > 0 and counter % k == 0:
#

print(f"[{result}]")
