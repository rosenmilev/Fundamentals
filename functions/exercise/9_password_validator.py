def password_validator(password):
    first_rule = True
    second_rule = True
    third_rule = True
    digit_number = 0
    if not 6 <= len(password) <= 10:
        first_rule = False
    for digit in password:
        if not digit.isalnum():
            second_rule = False
        if digit.isnumeric():
            digit_number += 1
    if digit_number < 2:
        third_rule = False
    if first_rule and second_rule and third_rule:
        print("Password is valid")
    else:
        if not first_rule:
            print("Password must be between 6 and 10 characters")
        if not second_rule:
            print("Password must consist only of letters and digits")
        if not third_rule:
            print("Password must have at least 2 digits")


curr_password = input()
password_validator(curr_password)
