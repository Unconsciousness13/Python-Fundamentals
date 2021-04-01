count_order = int(input())
total = 0
for order in range(count_order):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    price = ((days * capsule_count) * price_per_capsule)
    total += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total:.2f}")