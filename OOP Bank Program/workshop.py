# OOP Banking System

'''
    Overview:
        - Users can create accounts
        - Perform transactions like deposits, withdrawals, and balance inquiries
        - Basic Validation (Ensuring that withdrawals do not exceed the account balance)
'''

# 1. Create a BankAccount class: Represent an account with attributes such as the account holder's name, balance, and methods to perform transactions
class BankAccount:
    # constructor method
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
        
    # methods to perform the transactions (deposit, withdrawal, check_balance)
    
    # deposit method
    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
            print(f'${amount:.2f} added to your account! Your new balance is: ${self.balance:.2f}!')
        else:
            print('Deposit amount must be greater than zero!')
            
    # withdrawal method
    def withdrawal(self, amount):
        if (amount > 0):
            if (self.balance > amount):
                self.balance -= amount
                print(f'You withdrew ${amount:.2f}! Your remaining balance is: ${self.balance:.2f}')
            else:
                print('Insufficient balance!')
        else:
            print('Withdrawal amount must be greater than zero!')
    
    # check_balance method
    def check_balance(self):
        print(f'Account Holder: {self.account_holder}, Current Balance: ${self.balance:.2f}')
    

# 2. Create a Bank class: Will manage multiple accounts, allowing users to open new accounts and interact with their account.
class Bank:
    # constructor method
    def __init__(self):
        self.accounts = {}
        
    # create_account method
    def create_account(self, account_holder):
        if (account_holder not in self.accounts):
            new_account = BankAccount(account_holder)
            self.accounts[account_holder] = new_account
            print(f'Account created for {account_holder}!')
        else:
            print(f'Account already exists for {account_holder}!')
    
    # get_account method
    def get_account(self, account_holder):
        if (account_holder in self.accounts):
            return self.accounts[account_holder]
        else:
            print(f'Account for {account_holder} does not exist!')

# Create a CLI(also known as a "runner") to interact with the bank system
def runner():
    # create an instance of the Bank class
    bank = Bank()
    # while loop for continuous interactivity
    while True:
        # print valid options to the command line
        print('''
                ********** Bank Menu **********
                1. Create Account
                2. Deposit Money
                3. Withdrawal Money
                4. Check Balance
                5. Exit
              ''')
        # ask the user for input
        choice = input('What would you like to do today? (Choose a number) ')

        if (choice == '1'):
            name = input('What is the name of the Account Holder? ')
            bank.create_account(name)
        elif (choice == '2'):
            name = input('What is the name of the Account Holder? ')
            account = bank.get_account(name)
            if account:
                amount = float(input('How much would you like to deposit? '))
                account.deposit(amount)
        elif (choice == '3'):
            name = input('What is the name of the Account Holder? ')
            account = bank.get_account(name)
            if account:
                amount = float(input('How much would you like to withdrawal? '))
                account.withdrawal(amount)
        elif (choice == '4'):
            name = input('What is the name of the Account Holder? ')
            account = bank.get_account(name)
            if account:
                account.check_balance()
        elif (choice == '5'):
            print('Thank you for Banking with us! Have a good day!')
            break
        else:
            print('Invalid choice! Please try again!')
# run our program
runner()