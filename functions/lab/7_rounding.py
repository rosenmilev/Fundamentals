def rounding_func(nums):
    nums = list(map(round, map(float, nums)))
    return print(nums)


curr_nums = input().split()
rounding_func(curr_nums)
