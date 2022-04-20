class BankAccount: 

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("Insuficiant Funds: No interest rate applied")
        return self


    @classmethod
    def sum_all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

account1 = BankAccount(.03,600)
account2 = BankAccount(.01,200)

account1.deposit(1000).deposit(2000).deposit(5000).withdrawal(3000).yield_interest().display_account_info()
account2.deposit(80).deposit(200).withdrawal(100).withdrawal(300).withdrawal(50).withdrawal(100).yield_interest().display_account_info()

print(BankAccount.sum_all_balances())



class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            'checking' : BankAccount(.03, 0),
            'savings' : BankAccount(.01, 0)
        }

    def make_deposit(self, amount, account_type):
        self.account[account_type].deposit(amount)
        return self


    def make_withdrawal(self,amount, account_type):
        self.account[account_type].withdrawal(amount)
        return self

    def display_user_balance(self, account_type):
        print(f"User: {self.name}")
        self.account[account_type].display_account_info()
        return self

Sanoma = User('Sanoma')
Trinity = User('Trinity')
Alexander = User("Alexander")

Sanoma.make_deposit(1000, 'savings')
Sanoma.make_deposit(2000, 'savings')
Sanoma.make_deposit(5000, 'checking')
Sanoma.make_withdrawal(3000, 'checking')
Sanoma.display_user_balance('checking')

Trinity.make_deposit(600, 'savings')
Trinity.make_deposit(200, 'savings')
Trinity.make_withdrawal(100, 'savings')
Trinity.make_withdrawal(300, 'savings')
Trinity.display_user_balance('savings')

Alexander.make_deposit(300, 'checking')
Alexander.make_withdrawal(20, 'checking')
Alexander.make_withdrawal(50, 'checking')
Alexander.make_withdrawal(30, 'checking')
Alexander.display_user_balance('checking')

