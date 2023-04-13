class BankAccount:
    """

    """
    def __init__(self, accountnumber: int, name, balance: int): #How to convert str to int automatically? Check this
        self.accountnumber = accountnumber
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Name: {self.name}; " \
               f"ID number: {self.accountnumber}; " \
               f"Current balance: {self.balance}"

    def deposit(self, addmoney):
        self.balance = self.balance + addmoney
        return f"Transaction complete. Your balance now is: {self.balance}."

    def withdrawal(self, withdrawmoney):
        if withdrawmoney > self.balance:
            return f"Insufficient funds! Your balance is {self.balance}."
        else:
            self.balance -= withdrawmoney
        return f"Transaction complete."

    def bankfes(self):
        #Let's assume that the Bank Fee applies to withdrawals only
        if self.withdrawal():
            self.balance = self.balance * 0.95


    def display(self):
        pass



john = BankAccount(1, "John", 50)
mike = BankAccount(2, "Michael", 80)
example = BankAccount(input("Enter ID number"), input("Enter the name"), input("Enter the balance"))
# print(john.withdrawal(10))
# print(john)
print(example)
print(example.withdrawal(35))

