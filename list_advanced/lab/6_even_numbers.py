curr_list = input().split(", ")
curr_list = list(map(int, curr_list))

print([i for i in range(len(curr_list)) if curr_list[i] % 2 == 0])