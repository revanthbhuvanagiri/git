class atm:
    def __init__(self,name,balance,account_type):
        self.name = name
        self.balance = balance
        self.account_type = account_type
    def person(self):
        if self.name == "revanth" or 'Revanth':
            print("Hi Admin")
        else:
            print("Hi user")
    def user_account_type(self):
        if self.account_type == "savings":
            print("You are using saving account")
        else:
            print("You are using Business account")
    
    def deposit(self,amount):
        self.balance +=amount
        print(f'We successfully desposited the amount {amount} and total available balance is {self.balance}')
    
    def withdraw_money(self,amount):
        if self.balance < amount:
            print("Sorry, Your balance is less than the amount you entered")
        else:
            self.balance-=amount
            print(f"You have withdrawing amount {amount} and your current balance is {self.balance} ")


rev=atm("revanth",2,"business")
rev.withdraw_money(100)
rev.deposit(100)
rev.withdraw_money(52)
