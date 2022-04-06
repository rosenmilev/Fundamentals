import string

permitted_symbols = string.ascii_lowercase + string.ascii_uppercase + "-" + "_" + string.digits


def valid_username(username):
    is_valid = True

    if not 3 <= len(username) <= 16:
        is_valid = False

    if is_valid:
        for digit in username:
            if digit not in permitted_symbols:
                is_valid = False
                break

    # if not username[0].isalpha() or not username[-1].isalpha():
    #     is_valid = False

    return is_valid


usernames = input().split(", ")

for username in usernames:
    if valid_username(username):
        print(username)
