first = input().split(", ")
second = input().split(", ")
new_list = [stri for stri in first for word in second if stri in word]
print(sorted(set(new_list), key=new_list.index))
