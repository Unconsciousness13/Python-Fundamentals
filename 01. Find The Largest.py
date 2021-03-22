number = input()
max_num = ""
index = 0

digits_list = list(number)
digits_list.sort(reverse=True)

for i in range(len(number)):
    digit = digits_list[index]
    max_num += digit
    index += 1
print(max_num)