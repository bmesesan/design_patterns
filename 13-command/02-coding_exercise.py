# Command Coding Exercise
# Implement the Account.process()  method to process different account commands.

# The rules are obvious:

# success indicates whether the operation was successful

# You can only withdraw money if you have enough in your account

from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False
    
    def invoke(self, account):
        if self.action == self.Action.DEPOSIT:
            self.success = account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.success = account.withdraw(self.amount)
        else:
            raise NotImplementedError

        
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def process(self, command: Command):
        command.invoke(self)