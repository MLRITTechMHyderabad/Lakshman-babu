# import pylint+

#CI-CD :- Continuous Integration/Continuous Deployment

# cmd > pylint filename.py

"""
C - Convention
R - Refactor
W - Warning
E - Errors
F - Fatal
Tools: sonorlint etc..
"""

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def depoist(self, amount):
        self.__balance += amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance

account = Account("alice", 5000)

print(account.get_balance())
print(account.depoist(500))


