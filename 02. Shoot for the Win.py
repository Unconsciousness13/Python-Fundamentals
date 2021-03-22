list_target = list(map(int, input().split(" ")))
counter = 0
while True:
    command = input()
    if command == "End":
        print(f"Shot targets: {counter} -> {' '.join(map(str, list_target))}")
        break
    int_command = int(command)
    if int_command < len(list_target) and list_target[int_command] > -1:
        value = list_target[int_command]

        for i, num in (enumerate(list_target)):
            if num == -1:
                num = -1
            elif value < num:
                list_target[i] -= value
            elif value >= num and num > -1:
                list_target[i] += value
        list_target[int_command] = -1
        counter += 1
