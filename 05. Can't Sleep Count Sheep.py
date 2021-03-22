command = input()
coffee_needed = 0
counter_commands = 0

while not command == "END":
    if command in ["coding", "cat", "dog", "movie"]:
        coffee_needed += 1
        counter_commands += 1
    elif command in ["CODING", "CAT", "DOG", "MOVIE"]:
        coffee_needed += 2
        counter_commands += 1
    else:
        counter_commands += 1

    command = input()

if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)