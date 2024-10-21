class BankAcc():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance


    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc1 = BankAcc("John", 100)
acc1.deposit(50)
print(acc1.get_balance())


acc2 = BankAcc("Mary", 100)
acc2.deposit(150)
print(acc2.get_balance())