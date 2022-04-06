def min_max_sum(num):
    num = list(map(int, num))
    return print(f"The minimum number is {min(num)}\nThe maximum number is {max(num)}\nThe sum number is: {sum(num)}")


curr_nums = input().split()
min_max_sum(curr_nums)
