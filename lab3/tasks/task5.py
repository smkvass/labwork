#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. 
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
class MyBank:
    def __init__(self):
        self.owner_name = input("Enter owner's_name: ")
        self.balance = float(input("Enter initial balance: "))
        
    def name(self):
        print(f"Owner's name: {self.owner_name}")
        
    def balancce(self):
        print(f"Owner's balance: {self.balance:.2f} TG")
    
    def method1(self, money):
        self.balance += money
        print(f"Deposited {money:.2f}.TG New balance: {self.balance:.2f} TG")
    
    def method2(self, money):
        if money <= self.balance:
            self.balance -= money
            print(f"Withdrawal {money:.2f}.TG New balance: {self.balance:.2f} TG")
        else:
            print("Withdrawal amount exceeds available balance")


bank = MyBank()
bank.name()
bank.balancce()

deposit_money = float(input("Enter deposit: "))
bank.method1(deposit_money)

withdrawal_money = float(input("Enter withdrawal: "))
bank.method2(withdrawal_money)