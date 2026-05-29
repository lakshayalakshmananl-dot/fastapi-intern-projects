import json
import asyncio


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    # Async method to save account data
    async def save_to_file(self):
        account_data = {
            "account_holder": self.account_holder,
            "balance": self.balance
        }

        try:
            await asyncio.sleep(1)

            with open("account_data.json", "w") as file:
                json.dump(account_data, file, indent=4)

            print("Account data saved successfully!")

        except Exception as e:
            print("Error saving file:", e)

    # Async method to load account data
    async def load_from_file(self):
        try:
            await asyncio.sleep(1)

            with open("account_data.json", "r") as file:
                data = json.load(file)

            self.account_holder = data["account_holder"]
            self.balance = data["balance"]

            print("Account data loaded successfully!")

        except FileNotFoundError:
            print("File not found!")

        except json.JSONDecodeError:
            print("Invalid JSON data!")

        except Exception as e:
            print("Error loading file:", e)


async def main():
    account = BankAccount("Lakshaya", 5000)

    account.deposit(2000)
    account.withdraw(1000)
    account.display_balance()

    # Save data
    await account.save_to_file()

    print("\nLoading saved data...\n")

    # Create new object
    new_account = BankAccount("", 0)

    # Load saved data
    await new_account.load_from_file()

    new_account.display_balance()


asyncio.run(main())