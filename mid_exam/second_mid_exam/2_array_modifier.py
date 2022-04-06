def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]
    return nums


def multiply(nums, index1, index2):
    nums[index1] = nums[index1] * nums[index2]
    return nums


def decrease(nums):
    for i in range(len(nums)):
        nums[i] -= 1
    return nums


current_nums = input().split()


while True:
    command = input().split()
    current_nums = list(map(int, current_nums))

    if command[0] == "end":
        break
    if command[0] == "swap":
        current_nums = swap(current_nums, int(command[1]), int(command[2]))
    elif command[0] == "multiply":
        current_nums = multiply(current_nums, int(command[1]), int(command[2]))
    elif command[0] == "decrease":
        current_nums = decrease(current_nums)

current_nums = ", ".join(list(map(str, current_nums)))
print(current_nums)
