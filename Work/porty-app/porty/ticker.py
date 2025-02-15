# ticker.py
#
# Exercise 6.10: Making more pipeline components
'''
from follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield[func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows

if __name__ == "__main__":
    lines = follow("Data/stocklog.csv")
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
'''

# Exercise 6.11: Filtering data
'''
from follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield[func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row["name"] in names:
            yield(row)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows

if __name__ == "__main__":
    import report
    portfolio = report.read_portfolio("Data/portfolio.csv")
    rows = parse_stock_data(follow("Data/stocklog.csv"))
    rows = filter_symbols(rows, portfolio)
    for row in  rows:
        print(row)
'''

# Exercise 6.12: Putting it all together
'''
from follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield[func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row["name"] in names:
            yield(row)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows

def ticker(portfile, logfile, fmt):
    import report
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)
    import tableformat
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])
    

if __name__ == "__main__":
    import report
    portfolio = report.read_portfolio("Data/portfolio.csv")
    rows = parse_stock_data(follow("Data/stocklog.csv"))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
'''

# Exercise 6.15: Code simplification
'''
from follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield[func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows

def ticker(portfile, logfile, fmt):
    import report
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row["name"] in portfolio)
    import tableformat
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])
    

if __name__ == "__main__":
    import report
    portfolio = report.read_portfolio("Data/portfolio.csv")
    rows = parse_stock_data(follow("Data/stocklog.csv"))
    rows = (row for row in rows if row["name"] in portfolio)
    for row in rows:
        print(row)
'''

# Exercise 9.1: Making a simple package

from . follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield[func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows

def ticker(portfile, logfile, fmt):
    import report
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row["name"] in portfolio)
    import tableformat
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])
    

if __name__ == "__main__":
    import report
    portfolio = report.read_portfolio("Data/portfolio.csv")
    rows = parse_stock_data(follow("Data/stocklog.csv"))
    rows = (row for row in rows if row["name"] in portfolio)
    for row in rows:
        print(row)