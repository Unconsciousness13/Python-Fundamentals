import math

employer_one = int(input())
employer_two = int(input())
employer_three = int(input())
student_count = int(input())
employers_total_per_hour = employer_three + employer_two + employer_one
all = 0
while student_count > 0:
    student_count -= employers_total_per_hour
    all += 1
    if all % 4 == 0:
        all += 1
print(f"Time needed: {all}h.")
