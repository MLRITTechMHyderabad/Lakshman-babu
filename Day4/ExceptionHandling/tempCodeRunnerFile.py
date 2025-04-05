class InsufficientFundsError(Exception):
#     def __init__(self, Message):
#         self.Mesg = Message
#         super().__init__(Message)

# class BankAccount:
#     def __init__(self, Balance):
#         self.bal = Balance
#     def withdrawal(self, amount):
#         min_bal = float(input("Enter the minimum amount: "))
#         try:
#             if amount >= min_bal:
#                 raise ValueError("Error: Amount should be greater than minimum balance")
#             elif amount <= min_bal:
#                 raise InsufficientFundsError(" Error:  INSUFFICIENT FUNDS.")
#         except ValueError as v:
#             print(v)
#         except InsufficientFundsError as funds:
#             print(funds)
#         except Exception as E:
#             print(E)

# try:
#     Amount = float(input("Enter the Amount to Withdrawal: "))
#     To  
