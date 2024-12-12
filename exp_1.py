class BankAccount:
    def __init__(self, name, account_number, account_type, balance):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount):
        """Method to deposit an amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Method to withdraw an amount from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    
    def display_details(self):
        """Method to display account details."""
        print(f"\nAccount Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

print("Enter account details to create a new account:")

name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
account_type = input("Enter account type (e.g., Savings, Current): ")
balance = float(input("Enter initial balance: "))


account1 = BankAccount(name, account_number, account_type, balance)


account1.display_details()


while True:
    print("\nChoose an operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Details")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        deposit_amount = float(input("Enter deposit amount: "))
        account1.deposit(deposit_amount)
    elif choice == "2":
        withdraw_amount = float(input("Enter withdrawal amount: "))
        account1.withdraw(withdraw_amount)
    elif choice == "3":
        account1.display_details()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

