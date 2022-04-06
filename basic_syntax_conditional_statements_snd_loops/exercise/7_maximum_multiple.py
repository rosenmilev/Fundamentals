# divisor = int(input())
# boundary = int(input())
#
# N = 0
#
# for number in range(0, boundary + 1):
#     if number % divisor == 0:
#         N = number
#
# print(N)
#
# SECOND WAY
divisor = int(input())
boundary = int(input())

result = int(boundary / divisor) * divisor

print(result)