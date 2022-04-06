def palindrome_checker(input_nums):
    for num in input_nums:
        if num == num[::-1]:
            print(True)
        else:
            print(False)


nums = input().split(", ")
palindrome_checker(nums)
