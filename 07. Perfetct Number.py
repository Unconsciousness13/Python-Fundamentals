def perfect_number(num):
    prop_div = []
    for n in range(1, + num):
        if num % n == 0:
            prop_div.append(n)
    if sum(prop_div) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
    return num


number = int(input())
perfect_number(number)
