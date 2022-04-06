number = int(input())

is_prime = True

for digit in range(1, number):
    if number % digit == 0 and not digit == 1:
        is_prime = False

if is_prime:
    print("True")
else:
    print("False")
