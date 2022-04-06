def perfect_number(num):
    sum_of_dividers = 0
    for divider in range(1, num):
        if num % divider == 0:
            sum_of_dividers += divider
    if num == sum_of_dividers:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


curr_num = int(input())
perfect_number(curr_num)
