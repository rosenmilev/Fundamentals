input_data = input().split()
manipulated_list = []

while True:
    command = input().split()
    if command[0] == "end":
        break
    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(input_data):
            manipulated_list = input_data[int(command[1]) + 1:] + input_data[:int(command[1]) + 1]
            input_data = manipulated_list
        else:
            print("Invalid index")
            continue

    all_evens = list(filter(lambda p: p % 2 == 0, map(int, input_data)))
    all_odds = list(filter(lambda p: p % 2 == 1, map(int, input_data)))

    if command[0] == "max":
        if command[1] == "even":
            if len(all_evens) < 1:
                print("No matches")
            else:
                max_even = str(max(all_evens))
                if input_data.count(max_even) > 1:
                    input_data.reverse()
                    print(len(input_data) - 1 - input_data.index(max_even))
                    input_data.reverse()
                else:
                    print(input_data.index(max_even))

        elif command[1] == "odd":
            if len(all_odds) < 1:
                print("No matches")
            else:
                max_odd = str(max(all_odds))
                if input_data.count(max_odd) > 1:
                    input_data.reverse()
                    print(len(input_data) - 1 - input_data.index(max_odd))
                    input_data.reverse()
                else:
                    print(input_data.index(max_odd))

    elif command[0] == "min":
        if command[1] == "even":
            if len(all_evens) < 1:
                print("No matches")
            else:
                min_even = str(min(all_evens))
                if input_data.count(min_even) > 1:
                    input_data.reverse()
                    print(len(input_data) - 1 - input_data.index(min_even))
                    input_data.reverse()
                else:
                    print(input_data.index(min_even))
        elif command[1] == "odd":
            if len(all_odds) < 1:
                print("No matches")
            else:
                min_odd = str(max(all_odds))
                if input_data.count(min_odd) > 1:
                    input_data.reverse()
                    print(len(input_data) - 1 - input_data.index(min_odd))
                    input_data.reverse()
                else:
                    print(input_data.index(min_odd))

    elif command[0] == "first":
        if command[2] == "even":
            if int(command[1]) > len(input_data):
                print("Invalid count")
            else:
                print(all_evens[:int(command[1])])
        elif command[2] == "odd":
            if int(command[1]) > len(input_data):
                print("Invalid count")
            else:
                print(all_odds[:int(command[1])])

    elif command[0] == "last":
        if command[2] == "even":
            if int(command[1]) > len(input_data):
                print("Invalid count")
            else:
                all_evens.reverse()
                last_evens = all_evens[:int(command[1])]
                last_evens.reverse()
                print(last_evens)
        elif command[2] == "odd":
            if int(command[1]) > len(input_data):
                print("Invalid count")
            else:
                all_odds.reverse()
                last_odds = all_odds[:int(command[1])]
                last_odds.reverse()
                print(last_odds)

print(list(map(int, input_data)))
