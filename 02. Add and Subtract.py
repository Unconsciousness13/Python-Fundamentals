def sum_numbers(num1, num2):
    score = num1 + num2
    return score


def subtract(num3):
    result = num3 - sum_numbers
    return result


def add_and_subtract(f,s,t):
    total = sum_numbers(f,s) - third_num
    return total
    # sum_numbers()
    # subtract()


first_num = int(input())
second_num = int(input())
third_num = int(input())


print(add_and_subtract(first_num,second_num,third_num))
