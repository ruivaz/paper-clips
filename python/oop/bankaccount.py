class BankAccount:
  
  def __init__(self):
    self.balance = 0
  
  def withdraw(self, amount):
    self.balance -= amount
    return self.balance

  def deposit(self, amount):
    self.balance+= amount
    return self.balance

  def balanceof(self):
    print self.balance
  

a = BankAccount()
b = BankAccount()

a.deposit(50)
b.deposit(100)
a.withdraw(10)
b.deposit(100)

a.balanceof()
b.balanceof()
