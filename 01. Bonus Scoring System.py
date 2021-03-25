students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())
max_bonus = 0
max_attendance = 0
for i in range(students_count):
    attendances = int(input())
    total_bonus = attendances / lectures_count * (5 + initial_bonus)
    if max_bonus <= total_bonus:
        max_bonus = round(total_bonus)
        max_attendance = attendances
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_attendance} lectures.")
