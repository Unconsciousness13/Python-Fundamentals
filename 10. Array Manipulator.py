import sys

list_array = [int(x) for x in input().split()]
command = input()


def exchange(index):
    exchanged_array = list_array[index:] + list_array[:index]
    return exchanged_array


def show_index_max(list_of_nums):
    if not list_of_nums:
        print('No matches')
    else:
        max_num = -sys.maxsize
        for num in list_of_nums:
            if num > max_num:
                max_num = num
        index_rightmost_max = len(list_array) - 1 - list_array[::-1].index(max_num)
        print(index_rightmost_max)


def show_index_min(list_of_numbers):
    if not list_of_numbers:
        print('No matches')
    else:
        min_num = sys.maxsize
        for num in list_of_numbers:
            if num < min_num:
                min_num = num
        index_rightmost_min = len(list_array) - 1 - list_array[::-1].index(min_num)
        print(index_rightmost_min)


def show_first(list_nums, n):
    if n > len(list_array):  # potential edge case
        print("Invalid count")
    elif not list_nums:
        print(list_nums)
    else:
        list_of_firsts = list_nums[:n]
        print(list_of_firsts)


def show_last(list_nums, n):
    if n > len(list_array):  # potential edge case
        print("Invalid count")
    elif not list_nums:
        print(list_nums)
    else:
        list_nums = list_nums[::-1]
        list_of_lasts = list_nums[:n]
        print(list(reversed(list_of_lasts)))


while command != "end":
    curr_command = command.split()
    curr_task = curr_command[0]
    if curr_task == "exchange":
        index_to_split = int(curr_command[1])

        if 0 <= index_to_split < len(list_array):
            list_array = exchange(index_to_split + 1)
        else:
            print("Invalid index")

    elif curr_task == "max":
        type = curr_command[1]
        if type == 'even':
            even_elements = [x for x in list_array if x % 2 == 0]
            show_index_max(even_elements)
        elif type == 'odd':
            odd_elements = [x for x in list_array if x % 2 != 0]
            show_index_max(odd_elements)

    elif curr_task == "min":
        type = curr_command[1]
        if type == 'even':
            even_elements = [x for x in list_array if x % 2 == 0]
            show_index_min(even_elements)
        elif type == 'odd':
            odd_elements = [x for x in list_array if x % 2 != 0]
            show_index_min(odd_elements)

    elif curr_task == "first":
        type = curr_command[2]
        count = int(curr_command[1])
        if type == 'even':
            even_elements = [x for x in list_array if x % 2 == 0]
            show_first(even_elements, count)
        elif type == 'odd':
            odd_elements = [x for x in list_array if x % 2 != 0]
            show_first(odd_elements, count)
    elif curr_task == "last":
        type = curr_command[2]
        count = int(curr_command[1])
        if type == 'even':
            even_elements = [x for x in list_array if x % 2 == 0]
            show_last(even_elements, count)
        elif type == 'odd':
            odd_elements = [x for x in list_array if x % 2 != 0]
            show_last(odd_elements, count)
    command = input()

print(list_array)
