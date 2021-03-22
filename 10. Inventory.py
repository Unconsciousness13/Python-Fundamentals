def check_item_exist(items_list, item):
    if item in items_list:
        return True
    return False


def add_item(items_list, item):
    if not check_item_exist(items_list, item):
        items_list.append(item)
    return items_list


def remove_item(items_list, item):
    if check_item_exist(items_list, item):
        items_list.remove(item)
    return items_list


def combine_items(items_list, items_data):
    old_item, new_item = items_data.split(":")
    if check_item_exist(items_list, old_item):
        index_old_item = items_list.index(old_item)
        items_list.insert(index_old_item + 1, new_item)
    return items_list


def renew_item(items_list, item):
    if check_item_exist(items_list, item):
        items_list.remove(item)
        items_list.append(item)
    return items_list


items = input().split(", ")
command_data = input()

while not command_data == "Craft!":
    command, item = command_data.split(" - ")
    if command == "Collect":
        items = add_item(items, item)
    elif command == "Drop":
        items = remove_item(items, item)
    elif command == "Combine Items":
        items = combine_items(items, item)
    elif command == "Renew":
        items = renew_item(items, item)

    command_data = input()

print(*items, sep=", ")

# for index in range(len(items)):
#     if index == len(items) -1:
#         print(f"{items[index]}")
#     else:
#         print(f"{items[index]}, ", end='')