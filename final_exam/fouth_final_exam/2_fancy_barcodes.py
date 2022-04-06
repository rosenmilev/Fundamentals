import re

number_of_barcodes = int(input())

pattern = r"@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]@\#+"

pattern_2 = r"\d+"

for _ in range(number_of_barcodes):
    current_barcode = input()
    result = re.findall(pattern, current_barcode)

    if result:
        product_group = re.findall(pattern_2, current_barcode)
        if product_group:
            print(f"Product group: {''.join(product_group)}")
        else:
            print("Product group: 00")

    else:
        print("Invalid barcode")
