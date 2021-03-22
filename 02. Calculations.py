operator = input()
first_num = int(input())
second_num = int(input())


def operation(num_1, num_2, operator):
    result = None
    if operator == "multiply":
        result = num_1 * num_2
    elif operator == "divide":
        result = num_1 // num_2
    elif operator == "add":
        result = num_1 + num_2
    elif operator == "subtract":
        result = num_1 - num_2
    return result

print(operation(first_num,second_num,operator))
