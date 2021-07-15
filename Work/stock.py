# stock.py
#
# Exercise 4.1: Objects as Data Structures
'''
class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
'''

# Exercise 4.2: Adding some Methods

class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt