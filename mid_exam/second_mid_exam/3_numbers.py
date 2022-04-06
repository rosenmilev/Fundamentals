def greater_than_average(nums):
    greater_nums = []
    nums = list(map(int, nums))
    average_value = sum(nums) / len(nums)

    for num in nums:
        if num > average_value:
            greater_nums.append(num)

    if len(greater_nums) == 0:
        print("No")
    else:
        greater_nums = sorted(greater_nums, reverse=True)[:5]
    return " ".join(list(map(str, greater_nums)))


current_nums = input().split()
print(greater_than_average(current_nums))
