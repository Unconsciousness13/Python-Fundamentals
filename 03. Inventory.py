items = input().split(", ")
while True:
    command = input().split(" - ")
    if command[0] == "Craft!":
        print(", ".join(items))
        break
    elif command[0] == "Collect":
        if not command[-1] in items:
            items.append(command[-1])
    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[-1])
    elif command[0] == "Combine Items":
        old, new = command[-1].split(":")
        if old in items:
            i = items.index(old)
            i += 1
            items.insert(i, new)
    elif command[0] == "Renew":
        if command[1] in items:
            items.append(command[1])
            items.remove(command[1])
