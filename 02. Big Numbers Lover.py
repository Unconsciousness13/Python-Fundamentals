string_of_numbers = input().split()
new_list = sorted(string_of_numbers, reverse=True)
print("".join(new_list))