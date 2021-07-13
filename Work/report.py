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

# Exercise 2.6: Dictionaries as a container

def read_prices(filename):
    'reads a set of prices into a dictionary'
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print("Error: no such index")
    return prices

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
    