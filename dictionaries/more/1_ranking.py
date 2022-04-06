command = input()
contests = {}
results = {}
final = {}

while not command == "end of contests":

    command = command.split(":")
    contest = command[0]
    password_for_contest = command[1]

    contests[contest] = password_for_contest

    command = input()

command = input()

while not command == "end of submissions":

    command = command.split("=>")
    contest_to_check = command[0]
    password_to_check = command[1]
    username = command[2]
    points = int(command[3])

    if contest_to_check in contests and contests[contest_to_check] == password_to_check:
        if contest_to_check not in results:
            results[contest_to_check] = {}

        if username not in results[contest_to_check]:
            results[contest_to_check][username] = points

        else:
            if results[contest_to_check][username] < points:
                results[contest_to_check][username] = points
    command = input()

for contest in results:

    for user in results[contest]:
        if user not in final:
            a = 2
            # final[user] = results[contest][user]
        else:
            pass
            final[user] += results[contest][user]

final = dict(sorted(final.items(), key=lambda x: x[1], reverse=True))
best_candidate = list(final.keys())

print(f"Best candidate is {best_candidate[0]} with total {final[best_candidate[0]]} points.")
