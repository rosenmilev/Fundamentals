numbers = input().split(", ")
positives = ", ".join([i for i in numbers if int(i) >= 0])
negatives = ", ".join([i for i in numbers if int(i) < 0])
evens = ", ".join([i for i in numbers if int(i) % 2 == 0])
odds = ", ".join([i for i in numbers if not int(i) % 2 == 0])

print(f"Positive: {positives}")
print(f"Negative: {negatives}")
print(f"Even: {evens}")
print(f"Odd: {odds}")
