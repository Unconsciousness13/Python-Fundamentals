lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_broke = 0
expenses = 0
for num in range(1, lost_fights_count + 1):
    if num % 2 == 0:
        expenses += helmet_price
    if num % 3 == 0:
        expenses += sword_price
    if num % 2 == 0 and num % 3 == 0:
        expenses += shield_price
        shield_broke += 1

        if shield_broke % 2 == 0 and shield_price != 0:
            expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
