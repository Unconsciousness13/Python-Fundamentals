def eve_odd(res):
    sum_odd = 0
    sum_even = 0
    for num in res:
        rest = int(res)
        if int(num) % 2 == 0:
            sum_even += int(num)
        elif int(num) % 2 == 1:
            sum_odd += int(num)
    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")


number = int(input())
eve_odd(str(number))

