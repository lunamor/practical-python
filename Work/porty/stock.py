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
'''
class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt
'''

# Exercise 4.9: Better output for printing objects
'''
class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt
    
    def __repr__(self):
        return(f"Stock('{self.name}', {self.shares}, {self.price})")
'''

# Exercise 5.6: Simple Properties
'''
class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @ property
    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt
    
    def __repr__(self):
        return(f"Stock('{self.name}', {self.shares}, {self.price})")
'''

# Exercise 5.7: Properties and Setters
'''
class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._shares = shares

    def sell(self, amt):
        self.shares -= amt
    
    def __repr__(self):
        return(f"Stock('{self.name}', {self.shares}, {self.price})")
'''

# Exercise 5.8: Adding slots
'''
class Stock:

    __slots__ = ("name", "_shares", "price")

    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._shares = shares

    def sell(self, amt):
        self.shares -= amt
    
    def __repr__(self):
        return(f"Stock('{self.name}', {self.shares}, {self.price})")
'''

# Exercise 7.7: Using Closures to Avoid Repetition
'''
from typedproperty import typedproperty
class Stock:

    name = typedproperty("name", str)
    shares = typedproperty("shares", int)
    price = typedproperty("price", float)

    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt
    
    def __repr__(self):
        return(f"Stock('{self.name}', {self.shares}, {self.price})")
'''

# Exercise 7.8: Simplifying Function Calls
'''
from typedproperty import typedproperty
from typedproperty import String
from typedproperty import Integer
from typedproperty import Float

class Stock:

    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt
    
    def __repr__(self):
        return(f"Stock('{self.name}', {self.shares}, {self.price})")
'''

# Exercise 9.1: Making a simple package

from . typedproperty import typedproperty
from . typedproperty import String
from . typedproperty import Integer
from . typedproperty import Float

class Stock:

    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amt):
        self.shares -= amt
    
    def __repr__(self):
        return(f"Stock('{self.name}', {self.shares}, {self.price})")
