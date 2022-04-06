def calculations(a, b, operator):
    if operator == "multiply":
        print(a * b)
    elif operator == "divide":
        print(int(a / b))
    elif operator == "add":
        print(a + b)
    elif operator == "subtract":
        print(a - b)


curr_operator = input()
curr_a = int(input())
curr_b = int(input())

calculations(curr_a, curr_b, curr_operator)
