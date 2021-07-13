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