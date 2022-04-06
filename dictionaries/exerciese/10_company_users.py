employees_info = {}
command = input().split(" -> ")

while not command[0] == "End":
    company_name = command[0]
    employee_id = command[1]

    if company_name not in employees_info:
        employees_info[company_name] = []

    if employee_id not in employees_info[company_name]:
        employees_info[company_name].append(employee_id)

    command = input().split(" -> ")

for key in employees_info.keys():
    print(key)
    for employee in employees_info[key]:
        print(f"-- {employee}")
