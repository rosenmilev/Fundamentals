class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [i for i in self.products if i[0] == first_letter]

    def __repr__(self):
        message = ""
        message += f"Items in the {self.name} catalogue:\n"
        self.products = sorted(self.products)
        for i in range(len(self.products)):
            if i == len(self.products) - 1:
                message += f"{self.products[i]}"
            else:
                message += f"{self.products[i]}\n"
        return message

# Test code:
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
