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


class Invoice:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append(Product(name, price, quantity))

    def total_value(self):
        return sum(p.total_value() for p in self.products)

    def most_expensive(self):
        if not self.products:
            return None
        return max(self.products, key=lambda p: p.price)

    def display(self):
        print("Invoice details:")
        for p in self.products:
            p.description()
        print(f"Total invoice value: {self.total_value()} lei")


# Example usage:
invoice = Invoice()
invoice.add_product("Tigari",1, 2000)
invoice.add_product("Banane", 3, 50)
invoice.add_product("Mango", 3, 35)

invoice.display()
most_exp = invoice.most_expensive()
print(f"Most expensive product: {most_exp.name} ({most_exp.price} lei/unit)")
