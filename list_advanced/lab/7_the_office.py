happiness = input().split()
factor = int(input())
ref_happiness = list(map(lambda n: n * factor, map(int, happiness)))

happy_employees = [employee for employee in ref_happiness if employee > sum(ref_happiness) / len(ref_happiness)]

if len(happy_employees) >= len(ref_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(ref_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(ref_happiness)}. Employees are not happy!")
