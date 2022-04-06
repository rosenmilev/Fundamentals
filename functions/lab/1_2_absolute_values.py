def abs_values(input_nums):
    input_nums = list(map(float, input_nums))
    for num in range(len(input_nums)):
        if input_nums[num] < 0:
            input_nums[num] = abs(input_nums[num])
    return print(input_nums)


data = input().split()
abs_values(data)
