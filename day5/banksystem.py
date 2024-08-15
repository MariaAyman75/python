class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def generate_all_statements(self):
        statements = []
        for customer in self.customers:
            statements.append(customer.generate_statement())
        return statements

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, account_type, balance=0):
        account = Account(account_type, balance)
        self.accounts.append(account)
        return account

    def find_account(self, account_type):
        for account in self.accounts:
            if account.account_type == account_type:
                return account
        return None

    def transfer(self, from_account_type, to_account_type, amount):
        from_account = self.find_account(from_account_type)
        to_account = self.find_account(to_account_type)

        if from_account and to_account:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                return True
            else:
                print("Insufficient funds for transfer.")
                return False
        else:
            print("One or both accounts not found.")
            return False

    def generate_statement(self):
        statement = f"Customer: {self.name}\n"
        for account in self.accounts:
            statement += f"{account.account_type.capitalize()} Account: Balance = ${account.balance:.2f}\n"
        return statement
    
class Account:
    def __init__(self, account_type, balance=0):
        self.account_type = account_type
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

    def check_balance(self):
        return self.balance

bank = Bank("MyBank")

customer1 = Customer("Maria")
customer2 = Customer("Marina")
bank.add_customer(customer1)
bank.add_customer(customer2)

maria_checking = customer1.open_account("checking", 1000)
maria_savings = customer1.open_account("savings", 5000)

marina_checking = customer2.open_account("checking", 2000)

customer1.transfer("checking", "savings", 500)

print(f"maria's Checking Balance: ${maria_checking.check_balance():}")
print(f"maria's Savings Balance: ${maria_savings.check_balance():}")

for statement in bank.generate_all_statements():
    print(statement)
