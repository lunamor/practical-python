# pcost.py
#
# Exercise 1.27
'''
total = 0.00
with open("Data/portfolio.csv", "rt") as f:
    print("Exercise 1.27")
    headers = next(f)
    for line in f:
        row = line.split(",")
        cost = int(row[1]) * float(row[2][0:-1])
        total = total + cost
print(f"Total cost {total:0.2f}")
'''

# Exercise 1.30
'''
def portfolio_cost(filename):
    'compute the cost of shares'
    total = 0.00
    with open(filename, "rt") as f:
        headers = next(f)
        for line in f:
            row = line.split(",")
            cost = int(row[1]) * float(row[2][0:-1])
            total = total + cost
    return total

cost = portfolio_cost("Data/portfolio.csv")
print("total cost:", cost)
'''
# Exercise 1.31: Error handling
'''
def portfolio_cost(filename):
    'compute the cost of shares'
    total = 0.00
    with open(filename, "rt") as f:
        headers = next(f)
        for line in f:
            row = line.split(",")
            try:
                cost = int(row[1]) * float(row[2][0:-1])
                total = total + cost
            except ValueError:
                print("Error: Some fields are missing")
    return total

cost = portfolio_cost("Data/portfolio.csv")
print("total cost:", cost)
'''

# Exercise 1.32: Using a library function
'''
import csv

def portfolio_cost(filename):
    'compute the cost of shares'
    print('Exercise 1.32')
    total = 0.00
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                cost = int(row[1]) * float(row[2])
                total = total + cost
            except ValueError:
                print("Error: Some fields are missing")
    return total

cost = portfolio_cost("Data/portfolio.csv")
print("total cost:", cost)
'''

# Exercise 1.33: Reading from the command line
'''
import sys
import csv
def portfolio_cost(filename):
    'compute the cost of shares'
    print('Exercise 1.33')
    total = 0.00
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                cost = int(row[1]) * float(row[2])
                total = total + cost
            except ValueError:
                print("Error: Some fields are missing")
    return total
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)
'''

# Exercise 2.15: A practical enumerate() example
'''
import sys
import csv
def portfolio_cost(filename):
    'compute the cost of shares'
    print('Exercise 2.15')
    total = 0.00
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start = 1):
            try:
                cost = int(row[1]) * float(row[2])
                total = total + cost
            except ValueError:
                print(f"Row {i}: Couldn't convert: {row}")
    return total
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)
'''

# Exercise 2.16: Using the zip() function
'''
import sys
import csv
def portfolio_cost(filename):
    'compute the cost of shares'
    print("Exercise 2.16")
    total = 0.0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rownu, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                cost = int(record["shares"]) * float(record["price"])
                total += cost
            except ValueError:
                print(f"Row {rowno}: Couldn't convert: {row}")
    return total
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
cost = portfolio_cost(filename)
print("Total cost:", cost)
'''

# Exercise 3.14: Using more library imports
'''
import sys
from report import read_portfolio

def portfolio_cost(filename):
    'compute the cost of shares'
    total = 0.0
    portfolio = read_portfolio(filename)
    for holding in portfolio:
        total += holding["shares"] * holding["price"]
    return total
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
cost = portfolio_cost(filename)
print("Total cost:", cost)
'''

# Exercise 3.15: main() functions

from report import read_portfolio

def portfolio_cost(filename):
    'compute the cost of shares'
    total = 0.0
    portfolio = read_portfolio(filename)
    for holding in portfolio:
        total += holding["shares"] * holding["price"]
    return total

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    cost = portfolio_cost(args[1])
    print("Total cost:", cost)


# Exercise 3.16: Making Scripts
'''
import sys
from report import read_portfolio

def portfolio_cost(filename):
    'compute the cost of shares'
    total = 0.0
    portfolio = read_portfolio(filename)
    for holding in portfolio:
        total += holding["shares"] * holding["price"]
    return total

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    cost = portfolio_cost(args[1])
    print("Total cost:", cost)

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exercise 3.16: Making Scripts

import sys
from report import read_portfolio

def portfolio_cost(filename):
    'compute the cost of shares'
    total = 0.0
    portfolio = read_portfolio(filename)
    for holding in portfolio:
        total += holding.shares * holding.price
    return total

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    cost = portfolio_cost(args[1])
    print("Total cost:", cost)

if __name__ == "__main__":
    import sys
    main(sys.argv)