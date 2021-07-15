# fileparse.py
#
# Exercise 3.3: Reading CSV Files
'''
import csv

def parse_csv(filename):
    'Parse a CSV file into a list of records'
    with open(filename) as f:
        rows = csv.reader(f)
        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)
    return records
'''

# Exercise 3.4: Building a Column Selector
'''
import csv

def parse_csv(filename, select = None):
    'Parse a CSV file into a list of records'
    with open(filename) as f:
        rows = csv.reader(f)
        # Read the file headers
        headers = next(rows)
        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set fo headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row: 	# Skip row with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)
    return records
'''

# Exercise 3.5: Performing Type Conversion

import csv

def parse_csv(filename, select = None, types = None):
    'Parse a CSV file into a list of records'
    with open(filename) as f:
        rows = csv.reader(f)
        # Read the file headers
        headers = next(rows)
        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set fo headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row: 	# Skip row with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]
            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)
    return records