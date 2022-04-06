def even_or_odd(num, com):
    required_list = []

    if com == "even":
        for number in num:
            if number % 2 == 0:
                required_list.append(number)
    elif com == "odd":
        for number in num:
            if number % 2 == 1:
                required_list.append(number)
    return required_list


def min_max_number(evens_or_odds, min_or_max):
    if len(evens_or_odds) == 0:
        required_number = "No matches"
    elif min_or_max == "min":
        required_number = min(evens_or_odds)
    else:
        required_number = max(evens_or_odds)
    return required_number


def index_searching(total_data, min_or_max_number):
    required_index = 0
    if total_data.count(min_or_max_number) > 1:
        for num in range(len(total_data)):
            if total_data[num] == min_or_max_number:
                required_index = num
    else:
        required_index = total_data.index(min_or_max_number)
    return required_index


def first_last(evens_or_odds, count, comm, total_data):
    if int(count) > len(total_data):
        required_list = "Invalid count"
    else:
        if comm == "first":
            required_list = evens_or_odds[:int(count)]
        else:
            evens_or_odds.reverse()
            required_list = evens_or_odds[:int(count)]
            required_list.reverse()
    return required_list


input_data = input().split()
input_data = list(map(int, input_data))

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
    else:
        all_evens = even_or_odd(input_data, "even")
        all_odds = even_or_odd(input_data, "odd")

        if command[0] == "max":
            if command[1] == "even":
                requested_number = min_max_number(all_evens, "max")
                if requested_number == "No matches":
                    print(requested_number)
                else:
                    print(index_searching(input_data, requested_number))
            elif command[1] == "odd":
                requested_number = min_max_number(all_odds, "max")
                if requested_number == "No matches":
                    print(requested_number)
                else:
                    print(index_searching(input_data, requested_number))
        elif command[0] == "min":
            if command[1] == "even":
                requested_number = min_max_number(all_evens, "min")
                if requested_number == "No matches":
                    print(requested_number)
                else:
                    print(index_searching(input_data, requested_number))

            elif command[1] == "odd":
                requested_number = min_max_number(all_odds, "min")
                if requested_number == "No matches":
                    print(requested_number)
                else:
                    print(index_searching(input_data, requested_number))

        elif command[0] == "first" or command[0] == "last":
            if command[2] == "even":
                print(first_last(all_evens, command[1], command[0], input_data))
            elif command[2] == "odd":
                print(first_last(all_odds, command[1], command[0], input_data))

print(input_data)
