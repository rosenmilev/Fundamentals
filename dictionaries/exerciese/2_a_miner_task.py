# data = input()
# resources = {}
# counter = 1
#
# while not data == "stop":
#     if data not in resources and counter % 2 == 1:
#         resources[data] = 0
#         last_data = data
#     elif counter % 2 == 1:
#         last_data = data
#
#     if counter % 2 == 0:
#         resources[last_data] += int(data)
#
#     data = input()
#     counter += 1
#
# for res, quant in resources.items():
#     print(f"{res} -> {quant}")

# SECOND WAY

def minor_task():
    resources = {}

    while True:

        data = input()

        if data == "stop":
            break

        quantity = int(input())

        if data not in resources:
            resources[data] = quantity
        else:
            resources[data] += quantity

    for resource, quant in resources.items():
        print(f"{resource} -> {quant}")


minor_task()
