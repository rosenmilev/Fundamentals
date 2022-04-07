def tribonacci_sequence(number):
    n1, n2, n3 = 1, 1, 2
    numbers_to_print = ["1", "1", "2"]
    last_three_numbers = [n1, n2, n3]

    if number == 1:
        numbers_to_print = ["1"]

    elif number == 2:
        numbers_to_print = ["1", "1"]

    elif number == 3:
        numbers_to_print = ["1", "1", "2"]

    else:
        for _ in range(number - 3):
            n1 = n2
            n2 = n3
            n3 = sum(last_three_numbers)
            last_three_numbers = [n1, n2, n3]
            numbers_to_print.append(str(n3))

    return numbers_to_print


n = int(input())

print(" ".join(tribonacci_sequence(n)))
