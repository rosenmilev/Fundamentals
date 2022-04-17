input_data = input().split()
k = int(input())
counter = 1
index = 0
execution_order = []

while input_data:
    if index > len(input_data) - 1:
        index = 0
    if counter % k == 0 and counter > 0:
        execution_order.append(input_data[index])
        input_data.pop(index)
        index -= 1
    counter += 1
    index += 1

execution_order = ",".join(execution_order)
print(f"[{execution_order}]")
