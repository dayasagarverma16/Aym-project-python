class ATM:
    def __init__(self):
            # Initialize account balances and pins 
        self.accounts = {
            '123456': {'pin': '1111', 'balance': 1000},
            '654321': {'pin': '2222', 'balance': 500},
        }

    def login(self):
        account_number = input("Enter your account number: ")
        if account_number in self.accounts:
            pin = input("Enter your PIN: ")
            if self.accounts[account_number]['pin'] == pin:
                print("Login successful!")
                return account_number
            else:
                print("Incorrect PIN!")
        else:
            print("Account not found!")
        return None

    def check_balance(self, account_number):
        print(f"Your balance is: ${self.accounts[account_number]['balance']}")

    def deposit_money(self, account_number):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.accounts[account_number]['balance'] += amount
            print(f"${amount} deposited successfully!")
        else:
            print("Invalid deposit amount.")

    def withdraw_money(self, account_number):
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= self.accounts[account_number]['balance']:
            self.accounts[account_number]['balance'] -= amount
            print(f"${amount} withdrawn successfully!")
        else:
            print("Invalid amount or insufficient balance.")

    def run(self):
        print("Welcome to the ATM!")
        account_number = self.login()

        if account_number:
            while True:
                print("\n1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Exit")
                choice = input("Choose an option: ")

                if choice == '1':
                    self.check_balance(account_number)
                elif choice == '2':
                    self.deposit_money(account_number)
                elif choice == '3':
                    self.withdraw_money(account_number)
                elif choice == '4':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")


# Main Program
if __name__ == "__main__":
    atm = ATM()
    atm.run()
