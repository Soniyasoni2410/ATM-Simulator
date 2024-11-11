import datetime

class ATM:
    def __init__(self, name, pin, balance=0, account_type="savings", account_number="000000"):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.account_type = account_type
        self.account_number = account_number
        self.transaction_history = []
        self.bank_name = "State Bank of India"

    def check_balance(self):
        return f"Your current {self.account_type} account balance is: ₹{self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = f"Credited: ₹{amount:.2f} on {datetime.datetime.now()}"
            self.transaction_history.append(transaction)
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                transaction = f"Debited: ₹{amount:.2f} on {datetime.datetime.now()}"
                self.transaction_history.append(transaction)
                return True
            else:
                return False
        else:
            return False

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            return "PIN changed successfully."
        else:
            return "Incorrect old PIN."

    def show_transaction_history(self):
        if self.transaction_history:
            return "\n".join(self.transaction_history)
        else:
            return "No transactions made yet."

    def mini_statement(self):
        # Show the last 5 transactions for the mini statement
        recent_transactions = self.transaction_history[-5:]  # Get the last 5 transactions
        if recent_transactions:
            return "\n".join(recent_transactions)
        else:
            return "No transactions made yet."


def main():
    # Create an ATM instance with a default balance and PIN
    name = input("Enter your name: ")
    pin = input("Create your PIN: ")
    account_type = input("Select account type (savings/current): ").lower()
    balance = 10000  # Starting balance
    account_number = "123456789"  # Example account number

    atm = ATM(name=name, pin=pin, balance=balance, account_type=account_type, account_number=account_number)

    print("\nWelcome to the ATM Simulator")

    # User login
    entered_pin = input("Enter your PIN: ")

    if entered_pin == atm.pin:
        print(f"Login Successful! Welcome, {atm.name}!")

        while True:
            print("\nMain Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Mini Statement")
            print("7. Exit")

            choice = input("Select an option (1-7): ")

            if choice == "1":
                print(atm.check_balance())
            elif choice == "2":
                amount = float(input("Enter deposit amount (₹): "))
                if atm.deposit(amount):
                    print(f"₹{amount:.2f} deposited successfully.")
                else:
                    print("Invalid deposit amount.")
                print_user_info(atm)
            elif choice == "3":
                amount = float(input("Enter withdraw amount (₹): "))
                if atm.withdraw(amount):
                    print(f"₹{amount:.2f} withdrawn successfully.")
                else:
                    print("Insufficient balance or invalid withdrawal amount.")
                print_user_info(atm)
            elif choice == "4":
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                print(atm.change_pin(old_pin, new_pin))
            elif choice == "5":
                print("Transaction History:")
                print(atm.show_transaction_history())
            elif choice == "6":
                print("\nMini Statement:")
                print(atm.mini_statement())
            elif choice == "7":
                print("Exiting the ATM. Thank you!")
                break
            else:
                print("Invalid selection. Please try again.")
    else:
        print("Incorrect PIN. Please try again.")

def print_user_info(atm):
    print("\nAccount Information:")
    print(f"Name: {atm.name}")
    print(f"Account Type: {atm.account_type.capitalize()}")
    print(f"Balance: ₹{atm.balance:.2f}")
    print(f"Account Number: {atm.account_number}")
    print(f"Bank Name: {atm.bank_name}")

if __name__ == "__main__":
    main()


