class Product:
    def __init__(self, name='codetree', code=50):
        self.name = name
        self.code = code

name, code = input().split()

product1 = Product()
product2 = Product(name, code)

def print_product(product):
    print(f"product {product.code} is {product.name}")

print_product(product1)
print_product(product2)