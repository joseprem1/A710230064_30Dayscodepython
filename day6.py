class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def get_account_details(self):
        return f"Account Holder: {self.__account_holder}, Account Number: {self.__account_number}, Balance: {self.__balance}"

# Create a new bank account
account = BankAccount("123456789", "John Doe", 1000)

# Accessing and modifying the account balance using encapsulated methods
account.deposit(500)
account.withdraw(200)

# Trying to access the private attribute directly (will cause an error)
# print(account.__balance)

# Accessing account details through public method
print(account.get_account_details())