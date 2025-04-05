class InsufficientFundsError(Exception):
    def __init__(self, Message):
        self.Mesg = Message
        super().__init__(Message)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        try:
            if amount < 0:
                raise ValueError("Withdrawal amount cannot be negative.")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient funds in the account.")

            self.balance -= amount
            return f"Withdrawal successful. Remaining balance: {self.balance}"

        except ValueError as ve:
            return f"Error: {ve}"
        except InsufficientFundsError as ife:
            return f"Error: {ife}"
        except Exception as e:
            return f"Unexpected error: {e}"
        
try:
    initial_balance = float(input("Enter your initial bank balance: ₹"))
    withdraw_amount = float(input("Enter amount to withdraw: ₹"))

    account = BankAccount(initial_balance)

    result = account.withdraw(withdraw_amount)
    print(result)

except ValueError:
    print("Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"Something went wrong: {e}")