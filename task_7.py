# Simple Bank Account Class - Attributes: name, balance -   Methods: deposit(amount), withdraw(amount), get_balance()

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance
    

# Example usage
account = BankAccount("Moshiur", 100000)
account.deposit(5000)
account.withdraw(2000)
print(account.get_balance())  # Should return 103000
