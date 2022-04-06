def factorial_division(num):
    factorial = 1
    for digit in range(num, 0, -1):
        factorial *= digit
    return factorial


num1 = int(input())
num2 = int(input())
result = factorial_division(num1) / factorial_division(num2)
print(f"{result:.2f}")
