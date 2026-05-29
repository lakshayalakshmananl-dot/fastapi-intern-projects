class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance. Overdraft not allowed.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def get_balance(self):
        return self.balance


# Example usage
account1 = BankAccount("Lakshaya", 5000)

print("Account Owner:", account1.owner)

account1.deposit(2000)
account1.withdraw(1000)
account1.withdraw(7000)   # Overdraft attempt

print("Current Balance: ₹", account1.get_balance())