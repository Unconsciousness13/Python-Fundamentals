import re

string_locations = input()
pattern = r'(?P<sym>/|=)(?P<city>[A-Z][A-Za-z]{2,})(?P=sym)'
founded = []

for city in re.finditer(pattern, string_locations):
    citys = city.group('city')
    founded.append(citys)
print(f"Destinations: {', '.join(founded)}")
counter = sum([len(i) for i in founded])
print(f"Travel Points: {counter}")
