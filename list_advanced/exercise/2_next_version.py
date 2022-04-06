current_version = input().split(".")
current_version = list(map(int, current_version))
current_version[len(current_version) - 1] += 1

for i in range(len(current_version) - 1, 0, -1):
    if current_version[i] > 9:
        current_version[i] = 0
        current_version[i - 1] += 1

next_version = ".".join(list(map(str, current_version)))
print(next_version)
