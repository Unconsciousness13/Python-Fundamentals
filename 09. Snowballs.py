n = int(input())
snowball_value_max = 0
snowball_quality_max = 0
snowball_time_max = 0
snowball_snow_max = 0
for num in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int(snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > snowball_value_max:
        snowball_value_max = snowball_value
        snowball_quality_max = snowball_quality
        snowball_time_max = snowball_time
        snowball_snow_max = snowball_snow
print(f"{snowball_snow_max} : {snowball_time_max} = {int(snowball_value_max)} ({snowball_quality_max})")
