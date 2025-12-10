class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_vat(self):
        return self.price * 1.19

    def __str__(self):
        return f"{self.name}: {self.price_with_vat():.2f} lei (incl. VAT)"


class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def price_with_vat(self):
        discounted_price = self.price * (1 - self.discount)
        return discounted_price * 1.19

    def __str__(self):
        percent = int(self.discount * 100)
        return f"{self.name} (Discount {percent}%): {self.price_with_vat():.2f} lei (incl. VAT)"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total(self):
        return sum(p.price_with_vat() for p in self.products)

    def display(self):
        print("Shopping Cart:")
        for p in self.products:
            print(" -", p)
        print(f"Total to pay: {self.total():.2f} lei. Da banii ba, borfasule! ")


cart = ShoppingCart()
cart.add_product(Product("Paine", 5))
cart.add_product(Product("Castraveti", 3))
cart.add_product(DiscountedProduct("Tigari", 20, 0.25))
cart.add_product(DiscountedProduct("Ceapa", 10, 0.1))

cart.display()
