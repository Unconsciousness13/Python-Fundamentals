wagons = int(input())
lista = [0] * wagons
command = input()
while not command == "End":
    data = command.split()
    index = int(data[1])
    value = int(data [-1])
    if data[0] == "add":
        lista[-1] += value
    elif data[0] == "insert":
        lista[index] += value
    elif data[0] == "leave":
        lista[index] -= value
    command = input()
print(lista)