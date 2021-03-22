itte = int(input())
tank_capacity = 255
liters_full = 0
itte_count = 0
liters_in = int(input())
while not itte == itte_count:
    itte_count += 1
    liters_full += liters_in
    if liters_full > tank_capacity:
        print("Insufficient capacity!")
        liters_full -= liters_in

    if itte == itte_count:
        print(liters_full)
        break
    liters_in = int(input())