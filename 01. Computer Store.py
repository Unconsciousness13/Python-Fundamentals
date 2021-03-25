prices = input()
total = 0
taxes = 0
total_price = 0
while not prices == "special" or "regular":
    if prices == "special":
        if total == 0:
            print("Invalid order!")
            break
        total_price *= 0.90
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")
        break

    elif prices == "regular":
        if total == 0:
            print("Invalid order!")
            break
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")
        break
    number = float(prices)
    if float(prices) < 0:
        print("Invalid price!")
        total -= number

    total += number
    taxes = total * 0.2
    total_price = total + taxes

    prices = input()
