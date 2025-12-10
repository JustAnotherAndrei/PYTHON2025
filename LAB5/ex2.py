class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = float(balance)
        self.transactions = [f"Account opened with balance {self.balance:.2f}"]

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount:.2f}  | Balance: {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return
        if amount > self.balance:
            print("Error: Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append(f"Withdraw: -{amount:.2f} | Balance: {self.balance:.2f}")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if amount > self.balance:
            print("Error: Insufficient funds for transfer.")
            return
        self.balance -= amount
        other_account.balance += amount
        self.transactions.append(
            f"Transfer to {other_account.owner}: -{amount:.2f} | Balance: {self.balance:.2f}"
        )
        other_account.transactions.append(
            f"Transfer from {self.owner}: +{amount:.2f} | Balance: {other_account.balance:.2f}"
        )

    def history(self):
        print(f"~~~~~~ History for {self.owner} ~~~~~~")
        for line in self.transactions:
            print(line)
        print(f"Current balance: {self.balance:.2f}\n")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = float(interest_rate)

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        if interest == 0:
            self.transactions.append(f"Interest applied: +0.00 | Balance: {self.balance:.2f}")
            return
        self.balance += interest
        self.transactions.append(
            f"Interest ({self.interest_rate*100:.1f}%): +{interest:.2f} | Balance: {self.balance:.2f}"
        )


if __name__ == "__main__":
    a = BankAccount("Lucretiu", 200)
    b = SavingsAccount("Pastorel", 150, interest_rate=0.05)

    a.deposit(50)
    a.withdraw(30)
    a.transfer(b, 100)

    b.apply_interest()
    b.withdraw(20)

    a.history()
    b.history()
