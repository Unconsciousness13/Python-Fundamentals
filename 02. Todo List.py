command = input()
todo_list = [0] * 10
while not command == "End":
    priority, todo = command.split("-")
    priority = int(priority) - 1
    todo_list[priority] = todo

    command = input()
print([todo for todo in todo_list if not todo == 0])