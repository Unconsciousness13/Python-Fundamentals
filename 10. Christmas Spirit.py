quantity = int(input())
days = int(input())

budget = 0
total_spirit = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_spirit += 5
        budget += ornament_set * quantity
    if day % 3 == 0:
        total_spirit += 13
        budget += (quantity * tree_skirt + tree_garlands * quantity)
    if day % 5 == 0:
        total_spirit += 17
        budget += tree_lights * quantity
    if day % 10 == 0:
        total_spirit -= 20
        budget += tree_skirt + tree_garlands + tree_lights
    if day % 15 == 0:
        total_spirit += 30
if days % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
