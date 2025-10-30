class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def description(self):
        print(f"Product: {self.name}, Price: {self.price} lei, Quantity: {self.quantity}, Total value: {self.total_value()} lei")


# Example usage:
p = Product("Banane", 3, 16)
p.description()
p.update_quantity(20)
p.description()
