class Bank_acсount_system:
    def __init__(self, number, __balance):
        self.number = number
        self.balance = __balance

    def depositing(self, deposit):
        self.balance += deposit
        return self.balance

    def withdrawing(self, withdraw):
        self.balance -= withdraw
        return self.balance

    def get_balance(self):
        return self.balance


bank = Bank_acсount_system(123, 1000)
print(bank.depositing(20))
print(bank.withdrawing(30))
print(bank.get_balance())
