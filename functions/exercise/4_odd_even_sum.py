def odd_even_sum(num):
    even_sum = 0
    odd_sum = 0
    for digit_as_str in num:
        digit = int(digit_as_str)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = input()
odd_even_sum(number)
