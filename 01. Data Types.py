def transformation(one, two):
    if one == "int":
        result = int(two) * 2
        print(result)
    elif one == "real":
        result = float(two) * 1.50
        print(f"{result:.2f}")
    elif one == "string":
        print(f"${two}$")
    return one, two


first = input()
second = input()
transformation(first,second)