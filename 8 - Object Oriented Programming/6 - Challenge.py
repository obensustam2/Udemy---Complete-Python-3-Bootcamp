
class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


    def __str__(self):
        return f'Account Owner:{self.owner}, Balance:{self.balance}'


    def deposit(self, add):
        self.add = add
        self.balance += self.add
        print('Deposit is accepted')
        print(f'Balance is {self.balance}')
        return self.balance


    def withdraw(self, subtract):
        self.subtract = subtract
        self.balance -= self.subtract

        if self.balance < 0:
            print('Withdrawal is denied')
            self.balance += self.subtract
        else:
            print('Withdrawal is accepted')

        print(f'Balance is {self.balance}')
        return self.balance


my_account = Account('Oben', 1000)
print(my_account)
print(my_account.owner)
print(my_account.balance)
print()

my_account.deposit(20)
print()
my_account.withdraw(700)
print()
my_account.withdraw(500)



