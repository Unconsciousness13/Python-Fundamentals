race = list(int(num) for num in input().split())
racer_left = race[:len(race)//2]
racer_right = reversed(race[(len(race)//2 + 1):])
racer_right_time = 0
racer_left_time = 0
for number in racer_left:
    if not number == 0:
        racer_left_time += number
    else:
        racer_left_time *= 0.80
for number in racer_right:
    if not number == 0:
        racer_right_time += number
    else:
        racer_right_time *= 0.80
if racer_left_time < racer_right_time:
    print(f"The winner is left with total time: {racer_left_time:.1f}")
else:
    print(f"The winner is right with total time: {racer_right_time:.1f}")