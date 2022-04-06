year = int(input())
while True:
    year += 1
    special_year = True
    year_as_string = ""
    for digit in str(year):
        if digit in year_as_string:
            special_year = False
        year_as_string += digit
    if special_year:
        print(year)
        break
