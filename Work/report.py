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
'''
import csv

def read_portfolio(filename):
    'store portfolio in a list of dictionaries'
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row))
            stock = {
                "name" : record["name"],
                "shares" : int(record["shares"]),
                "price" : float(record["price"])
            }
            portfolio.append(stock)
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
        shares = stock["shares"]
        old_price = stock["price"]
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
'''

# Exercise 3.1: Structuring a program as a collection of functions
'''
import csv

def read_portfolio(filename):
    'store portfolio in a list of dictionaries'
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row))
            stock = {
                "name" : record["name"],
                "shares" : int(record["shares"]),
                "price" : float(record["price"])
            }
            portfolio.append(stock)
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
        shares = stock["shares"]
        old_price = stock["price"]
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print("%10s %10s %10s %10s" %headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        formatted_price = "$" + f"{price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")

portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
report = make_report(portfolio, prices)
print_report(report)
'''

# Exercise 3:2: Creating a top-level function for program execution
'''
import csv

def read_portfolio(filename):
    'store portfolio in a list of dictionaries'
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row))
            stock = {
                "name" : record["name"],
                "shares" : int(record["shares"]),
                "price" : float(record["price"])
            }
            portfolio.append(stock)
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
        shares = stock["shares"]
        old_price = stock["price"]
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(report):
    'print a report of the portfolio'
    headers = ('Name', 'Shares', 'Price', 'Change')
    print("%10s %10s %10s %10s" %headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        formatted_price = "$" + f"{price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")

def portfolio_report(portfolio_filename, prices_filename):
    'read portfolio and prioces, make and print report'
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report("Data/portfolio.csv", "Data/prices.csv")
'''

# Exercise 3.12: Using your library module
'''
from fileparse import parse_csv

def read_portfolio(filename):
    'store portfolio in a list of dictionaries'
    portfolio = parse_csv(filename, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
    return portfolio

def read_prices(filename):
    'reads a set of prices into a dictionary'
    prices = dict(parse_csv(filename, types=[str, float], has_headers=False))
    return prices

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

def print_report(report):
    'print a report of the portfolio'
    headers = ('Name', 'Shares', 'Price', 'Change')
    print("%10s %10s %10s %10s" %headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        formatted_price = "$" + f"{price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")

def portfolio_report(portfolio_filename, prices_filename):
    'read portfolio and prioces, make and print report'
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report("Data/portfolio.csv", "Data/prices.csv")
'''

# Exercise 3.15: main() functions
'''
from fileparse import parse_csv

def read_portfolio(filename):
    'store portfolio in a list of dictionaries'
    portfolio = parse_csv(filename, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
    return portfolio

def read_prices(filename):
    'reads a set of prices into a dictionary'
    prices = dict(parse_csv(filename, types=[str, float], has_headers=False))
    return prices

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

def print_report(report):
    'print a report of the portfolio'
    headers = ('Name', 'Shares', 'Price', 'Change')
    print("%10s %10s %10s %10s" %headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        formatted_price = "$" + f"{price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")

def portfolio_report(portfolio_filename, prices_filename):
    'read portfolio and prioces, make and print report'
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])
'''

# Exercise 3.16: Making Scripts
'''
from fileparse import parse_csv

def read_portfolio(filename):
    'store portfolio in a list of dictionaries'
    portfolio = parse_csv(filename, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
    return portfolio

def read_prices(filename):
    'reads a set of prices into a dictionary'
    prices = dict(parse_csv(filename, types=[str, float], has_headers=False))
    return prices

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

def print_report(report):
    'print a report of the portfolio'
    headers = ('Name', 'Shares', 'Price', 'Change')
    print("%10s %10s %10s %10s" %headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        formatted_price = "$" + f"{price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")

def portfolio_report(portfolio_filename, prices_filename):
    'read portfolio and prioces, make and print report'
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exercise 3.18: Fixing existing functions
'''
from fileparse import parse_csv

def read_portfolio(filename):
    'store portfolio in a list of dictionaries'
    with open(filename) as f:
        portfolio = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
    return portfolio

def read_prices(filename):
    'reads a set of prices into a dictionary'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices

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

def print_report(report):
    'print a report of the portfolio'
    headers = ('Name', 'Shares', 'Price', 'Change')
    print("%10s %10s %10s %10s" %headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        formatted_price = "$" + f"{price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")

def portfolio_report(portfolio_filename, prices_filename):
    'read portfolio and prioces, make and print report'
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exercise 4.4: Using your class
'''
from fileparse import parse_csv
import stock

def read_portfolio(filename):
    'store portfolio in a list of Stocks'
    with open(filename) as f:
        portfolio = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
        stocks = [stock.Stock(s["name"], s["shares"], s["price"]) for s in portfolio]
    return stocks

def read_prices(filename):
    'reads a set of prices into a dictionary'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices

def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock.name
        shares = stock.shares
        old_price = stock.price
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(report):
    'print a report of the portfolio'
    headers = ('Name', 'Shares', 'Price', 'Change')
    print("%10s %10s %10s %10s" %headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        formatted_price = "$" + f"{price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}")

def portfolio_report(portfolio_filename, prices_filename):
    'read portfolio and prioces, make and print report'
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exercise 4.4: An Extensibility Problem
'''
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename):
    'store portfolio in a list of Stocks'
    with open(filename) as f:
        portfolio = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
        stocks = [stock.Stock(s["name"], s["shares"], s["price"]) for s in portfolio]
    return stocks

def read_prices(filename):
    'reads a set of prices into a dictionary'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices

def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock.name
        shares = stock.shares
        old_price = stock.price
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(reportdata, formatter):
    'print a nicely formatted table from a list of (name, shares, price, change) tuples'
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename):
    'Make a stock report given portfolio and price data files'
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # Create a report data
    report = make_report(portfolio, prices)
    # Print it out
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exercise 4.6: Using Inheritance to Produce Different Output
'''
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename):
    'store portfolio in a list of Stocks'
    with open(filename) as f:
        portfolio = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
        stocks = [stock.Stock(s["name"], s["shares"], s["price"]) for s in portfolio]
    return stocks

def read_prices(filename):
    'reads a set of prices into a dictionary'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices

def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock.name
        shares = stock.shares
        old_price = stock.price
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(reportdata, formatter):
    'print a nicely formatted table from a list of (name, shares, price, change) tuples'
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename):
    'Make a stock report given portfolio and price data files'
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # Create a report data
    report = make_report(portfolio, prices)
    # Print it out
    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exercise 4.7: Polymorphism in Action
'''
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename):
    'store portfolio in a list of Stocks'
    with open(filename) as f:
        portfolio = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
        stocks = [stock.Stock(s["name"], s["shares"], s["price"]) for s in portfolio]
    return stocks

def read_prices(filename):
    'reads a set of prices into a dictionary'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices

def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock.name
        shares = stock.shares
        old_price = stock.price
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(reportdata, formatter):
    'print a nicely formatted table from a list of (name, shares, price, change) tuples'
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt = "txt"):
    'Make a stock report given portfolio and price data files'
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # Create a report data
    report = make_report(portfolio, prices)
    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exercise 4.8: Putting it all together
'''
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(filename):
    'store portfolio in a list of Stocks'
    with open(filename) as f:
        portfolio = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
        stocks = [stock.Stock(s["name"], s["shares"], s["price"]) for s in portfolio]
    return stocks

def read_prices(filename):
    'reads a set of prices into a dictionary'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices

def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock.name
        shares = stock.shares
        old_price = stock.price
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(reportdata, formatter):
    'print a nicely formatted table from a list of (name, shares, price, change) tuples'
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt = "txt"):
    'Make a stock report given portfolio and price data files'
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # Create a report data
    report = make_report(portfolio, prices)
    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exersice 6.2: Supporting Iteration
'''
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename):
    'read a stock portfolio file into a list of Stocks Stocks'
    with open(filename) as f:
        portdicts = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
        stocks = [Stock(s["name"], s["shares"], s["price"]) for s in portdicts]
    return Portfolio(stocks)

def read_prices(filename):
    'reads a set of prices into a dictionary'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices

def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock.name
        shares = stock.shares
        old_price = stock.price
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(reportdata, formatter):
    'print a nicely formatted table from a list of (name, shares, price, change) tuples'
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt = "txt"):
    'Make a stock report given portfolio and price data files'
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # Create a report data
    report = make_report(portfolio, prices)
    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exersice 7.3: Creating a list of instances
'''
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename):
    'read a stock portfolio file into a list of Stocks Stocks'
    with open(filename) as f:
        portdicts = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], has_headers=True)
        stocks = [Stock(**s) for s in portdicts]
    return Portfolio(stocks)

def read_prices(filename):
    'reads a set of prices into a dictionary'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices

def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock.name
        shares = stock.shares
        old_price = stock.price
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(reportdata, formatter):
    'print a nicely formatted table from a list of (name, shares, price, change) tuples'
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt = "txt"):
    'Make a stock report given portfolio and price data files'
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # Create a report data
    report = make_report(portfolio, prices)
    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
'''

# Exersice 7.4: Argument pass-through

from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat

def read_portfolio(filename, **opts):
    'read a stock portfolio file into a list of Stocks Stocks'
    with open(filename) as f:
        portdicts = parse_csv(f, select=["name", "shares", "price"], types=[str, int, float], has_headers=True, **opts)
        stocks = [Stock(**s) for s in portdicts]
    return Portfolio(stocks)

def read_prices(filename):
    'reads a set of prices into a dictionary'
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    return prices

def make_report(list_stocks, dict_prices):
    'takes a list of stocks and dictionary of prices and returns a list of tuples containing the name, # of shares, prices, and change'
    rows = []
    for stock in list_stocks:
        name = stock.name
        shares = stock.shares
        old_price = stock.price
        current_price = dict_prices[name]
        change = current_price - old_price
        rows.append((name, shares, current_price, change))
    return rows

def print_report(reportdata, formatter):
    'print a nicely formatted table from a list of (name, shares, price, change) tuples'
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt = "txt"):
    'Make a stock report given portfolio and price data files'
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # Create a report data
    report = make_report(portfolio, prices)
    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)