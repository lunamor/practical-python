# tableformat.py
#
# Exercise 4.5: An Extensibility Problem
'''
class TableFormatter:

    def headings(self, headers):
        'Emit the table headings.'
        raise NotImplementedError()

    def row(self, rowdata):
        'Emit a single row of table data'
        raise NotImplementedError()
'''

# Exercise 4.6: Using Inheritance to Produce Different Output
'''
class TextTableFormatter(TableFormatter):
    'Emit a table in plain-text format'
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end = " ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end = " ")
        print()

class CSVTableFormatter(TableFormatter):
    'Output portfolio data in CSV format.'
    def headings(self, headers):
        print(",".join(headers))
    def row(self, rowdata):
        print(",".join(rowdata))

class HTMLTableFormatter(TableFormatter):
    'Output portfolio data in HTML format'
    def headings(self, headers):
        print("<tr>", end = "")
        for h in headers:
            print(f"<th>{h}</th>", end = "")
        print("</tr>", end = "")
        print()
    def row(self, rowdata):
        print("<tr>", end = "")
        for d in rowdata:
            print(f"<td>{d}</td>", end = "")
        print("</tr>", end = "")
        print()
'''

# Exercise 4.7: Polymorphism is Action
'''
def create_formatter(name):
    if name == "txt":
        return TextTableFormatter()
    elif name == "csv":
        return CSVTableFormatter()
    elif name == "html":
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown format {fmt}")

# Exercise 4.10: An example of using getattr()

def print_table(data, colnames, formatter):
    formatter.headings(colnames)
    for stock in data:
        formatter.row([str(getattr(stock, colname)) for colname in colnames])
'''

# Exercise 4.11: Defining a custom exception

class TableFormatter:

    def headings(self, headers):
        'Emit the table headings.'
        raise NotImplementedError()

    def row(self, rowdata):
        'Emit a single row of table data'
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    'Emit a table in plain-text format'
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end = " ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end = " ")
        print()

class CSVTableFormatter(TableFormatter):
    'Output portfolio data in CSV format.'
    def headings(self, headers):
        print(",".join(headers))
    def row(self, rowdata):
        print(",".join(rowdata))

class HTMLTableFormatter(TableFormatter):
    'Output portfolio data in HTML format'
    def headings(self, headers):
        print("<tr>", end = "")
        for h in headers:
            print(f"<th>{h}</th>", end = "")
        print("</tr>", end = "")
        print()
    def row(self, rowdata):
        print("<tr>", end = "")
        for d in rowdata:
            print(f"<td>{d}</td>", end = "")
        print("</tr>", end = "")
        print()

class FormatError(Exception):
    pass

def create_formatter(name):
    if name == "txt":
        return TextTableFormatter()
    elif name == "csv":
        return CSVTableFormatter()
    elif name == "html":
        return HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown table format %s" %name)

# Exercise 4.10: An example of using getattr()

def print_table(data, colnames, formatter):
    formatter.headings(colnames)
    for stock in data:
        formatter.row([str(getattr(stock, colname)) for colname in colnames])
