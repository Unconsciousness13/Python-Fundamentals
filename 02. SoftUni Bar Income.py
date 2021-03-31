import re

name_pattern = r'(?<=\%)([A-Z][a-z]+)(?=\%)'
product_pattern = r'(?<=\<)([\w]+)(?=\>)'
quantity_pattern = r'(?<=\|)([\d]+)(?=\|)'
price_pattern = r'([\d]+(\.[\d]+)?)(?=\$)'
total = 0
command = input()
while not command == "end of shift":
    matched_name = re.findall(name_pattern, command)
    matched_product = re.findall(product_pattern, command)
    matched_quantity = re.findall(quantity_pattern, command)
    matched_price = re.findall(price_pattern, command)
    if matched_name and matched_product and matched_quantity and matched_price:
        for qua in matched_quantity:
            matched_quantity = int(qua)
        for pri in matched_price:
            for pr in pri:
                matched_price = float(pr)
                break
        total_for_user = matched_quantity * matched_price
        total += total_for_user
        for n in matched_name:
            matched_name = n
        for p in matched_product:
            matched_product = p
        print(f"{matched_name}: {matched_product} - {total_for_user:.2f}")
    command = input()
print(f"Total income: {total:.2f}")
