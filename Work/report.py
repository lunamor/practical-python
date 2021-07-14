# report.py
#
# Exercise 2.4: A list of tuples
'''
import csv

def read_portfolio(filename):
    'store portfolio in a list of tuples'
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio
'''

# Exercise 2.5: List of Dictionaries
'''
import csv

def read_portfolio(filename):
    'store portfolio in a list of dictionaries'
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)
    return portfolio
'''

# Exercise 2.6: Dictionaries as a container
'''
def read_prices(filename):
    'reads a set of prices into a dictionary'
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                errorStr = "Error: no such index"
    return prices
'''

# Exercise 2.7: Fingin out if you can retire

def calc_gain_loss(portfolio_file, current_values_file):
    'computes the current value of the portfolio along with the gain/loss'
    portfolio = read_portfolio(portfolio_file)
    current_prices = read_prices(current_values_file)

    old_portfolio_value = 0.0
    new_portfolio_value = 0.0
    for s in portfolio:
        old_portfolio_value += s["shares"] * s["price"]
        new_portfolio_value += s["shares"] * current_prices[s["name"]]
    return old_portfolio_value - new_portfolio_value
    

# Exercise 2.9: Collecting Data
'''
def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock["name"]
        shares = stock["shares"]
        old_price = stock["price"]
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows
'''
        
# Exercise 2.10: Printing a formatted table
'''
portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)
for name, shares, price, change in report:
     print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")
'''

# Exercise 2.11: Adding some headers
'''
headers = ('Name', 'Shares', 'Price', 'Change')
print("%10s %10s %10s %10s" %headers)
print(('-' * 10 + ' ') * len(headers))

portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)
for name, shares, price, change in report:
     print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")
'''

# Exercise 2.12: Formatting Challenge
'''
headers = ('Name', 'Shares', 'Price', 'Change')
print("%10s %10s %10s %10s" %headers)
print(('-' * 10 + ' ') * len(headers))

portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)
for name, shares, price, change in report:
    formatted_price = "$" + f"{price:0.2f}"
    print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")
'''

# Exercise 2.16: Using the zip() function

import csv

def read_portfolio(filename):
    'store portfolio in a list of dictionaries'
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = dict(zip(header, row))
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    'reads a set of prices into a dictionary'
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                errorStr = "Error: no such index"
    return prices

def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock["name"]
        shares = int(stock["shares"])
        old_price = float(stock["price"])
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

headers = ('Name', 'Shares', 'Price', 'Change')
print("%10s %10s %10s %10s" %headers)
print(('-' * 10 + ' ') * len(headers))

portfolio = read_portfolio("Data/portfoliodate.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)
for name, shares, price, change in report:
    formatted_price = "$" + f"{price:0.2f}"
    print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")