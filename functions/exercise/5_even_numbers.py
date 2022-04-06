def even_numbers(input_data):
    result = list(filter(lambda a: a % 2 == 0, map(int, input_data)))
    print(result)


numbers = input().split()
even_numbers(numbers)
