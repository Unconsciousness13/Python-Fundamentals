def orders(product, quantity):
    result = product * quantity
    if product == "coffee":
        result = 1.50 * quantity
    elif product == "water":
        result = 1 * quantity
    elif product == "coke":
        result = 1.40 * quantity
    elif product == "snacks":
        result = 2 * quantity
    return (f"{result:.2f}")


product_name = input()
volume = int(input())
print(orders(product_name, volume))
