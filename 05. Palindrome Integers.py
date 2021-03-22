def true_or_false(string_a):
    for num in list_str:
        if num == num[::-1]:
            print("True")
        else:
            print("False")
    return string_a


list_str = input().split(", ")
true_or_false(list_str)