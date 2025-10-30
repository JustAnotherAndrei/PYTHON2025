class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"{self.holder}'s balance: ${self.balance}")


# Example usage:
account = BankAccount("Ion Tiriac", 123454321)
account.deposit(99999999999)  #imobiliare alea alea
account.withdraw(1000000000000)  # Error: prea scump avionu csf, mistretu ba stanga, ba dreapta
account.withdraw(30)
account.display_balance()  # Ion Tiriac's balance