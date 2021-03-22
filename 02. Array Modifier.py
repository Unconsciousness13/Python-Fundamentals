array = input().split(" ")
array = list(map(int, array))
while True:
    command = input()
    action = command.split(" ")
    if command == "end":
        break
    if command == "decrease":
        for el in range(len(array)):
            array[el] = array[el] - 1

    if action[0] == "swap":
        first, second = int(action[1]), int(action[2])
        array[int(first)], array[int(second)], = array[int(second)], array[int(first)]
    if action[0] == "multiply":
        first, second = int(action[1]), int(action[2])
        array[first] = array[int(first)] * array[int(second)]
counter = 0
for num in array:
    counter += 1
    if counter == len(array):
        print(num, end="")
        break
    print(num, end=", ")
