list_of_numbers = input().split()
sep_list = list(int(x) for x in list_of_numbers)
text = input()
text = list(text)
final_word = ""
for index in range(len(sep_list)):
    cur_number = sep_list[index]
    result = (sum([int(i) for i in str(cur_number)]))
    irr = len(text)
    if result > irr:
        irr = result - irr
    else:
        irr = result
    for el in range(irr+1):
        letter = text[el]
        if el == irr:
            final_word += letter
            text.remove(letter)
print(final_word)
