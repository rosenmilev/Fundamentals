number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if number > 1000000:
        print("large positive")
    elif 0 < number < 1:
        print("small positive")
    else:
        print("positive")
elif number < 0:
    if number < -1000000:
        print("large negative")
    elif -1 < number < 0:
        print("small negative")
    else:
        print("negative")