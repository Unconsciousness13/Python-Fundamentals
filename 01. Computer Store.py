total = 0
taxes = total * 0.20
while True:
    command = input()

    if command == "regular" or command == "special":
        if total == 0:
            print("Invalid order!")
            break
    else:
        command = float(command)
        if command < 0:
            print("Invalid price!")
        else:

            total += command
            taxes += command * 0.20

    if command == "special":
        total_after_discount = total * 0.90
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_after_discount + (taxes * 0.90):.2f}$")
        break

    elif command == "regular":
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total + taxes:.2f}$")
        break
