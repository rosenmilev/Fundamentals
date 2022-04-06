year = int(input())

while True:
    year += 1
    if len(set(f"{year}")) == len(str(year)):
        print(year)
        break
