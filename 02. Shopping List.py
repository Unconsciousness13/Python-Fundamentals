initial_list = list(input().split("!"))

while True:
    command = input()
    comi = command.split()
    com, item = comi[0], comi[1],
    if command == "Go Shopping!":
        print(", ".join(initial_list))
        break
    if com == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)
    if com == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)
    if com == "Correct":
        if item in initial_list:
            i = initial_list.index(item)
            initial_list.pop(i)
            initial_list.insert(i, comi[-1])
    if com == "Rearrange":
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
