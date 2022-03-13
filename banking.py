# Parent Class: User
# Holds details about the user
# Function to show user details

# Child Class:Bank
# Stores details about the account balance
# Stores detauks about the amount
# Allows deposits, withdraw and view_balance

# Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)


# Child Class

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposits(self, amount: int):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account has been updated: ", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Fund: ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been update: ", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance is: ", self.balance)


Bob = Bank('Bob', 21, 'Male')


Bob.show_details()
Bob.deposits(50)
Bob.deposits(110)
Bob.deposits(40)
Bob.withdraw(210)
Bob.withdraw(100)
Bob.view_balance()
