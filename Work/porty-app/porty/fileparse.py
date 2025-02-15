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
'''
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
'''

# Exercise 3.6: Working without Headers
'''
import csv

def parse_csv(filename, select = None, types = None, has_headers = True):
    'Parse a CSV file into a list of records'
    with open(filename) as f:
        rows = csv.reader(f)
        if has_headers:
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
            if has_headers:
                # Make a dictionary
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records
'''

# Exercise 3.7: Picking a different column delimiter
'''
import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimiter = ","):
    'Parse a CSV file into a list of records'
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)
        if has_headers:
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
            if has_headers:
                # Make a dictionary
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records
'''

# Exercise 3.8: Raising exceptions
'''
import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimiter = ","):
    'Parse a CSV file into a list of records'
    # Raise exception if both the select and the has_headers=False arguments are passed
    if select and (not has_headers):
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)
        if has_headers:
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
        for rowno, row in enumerate(rows, 1):
            try:
                if not row: 	# Skip row with no data
                    continue
                # Filter the row if specific columns were selected
                if indices:
                    row = [row[index] for index in indices]
                if types:
                        row = [func(val) for func, val in zip(types, row)]
                if has_headers:
                    # Make a dictionary
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                print("Row", rowno, ": Couldn't convert", row)
                print("Row", rowno, ":", e)
        
    return records
'''

# Exercise 3.10: Silencing Errors
'''
import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimiter = ",", silence_errors = False):
    'Parse a CSV file into a list of records'
    # Raise exception if both the select and the has_headers=False arguments are passed
    if select and (not has_headers):
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)
        if has_headers:
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
        for rowno, row in enumerate(rows, 1):
            try:
                if not row: 	# Skip row with no data
                    continue
                # Filter the row if specific columns were selected
                if indices:
                    row = [row[index] for index in indices]
                if types:
                        row = [func(val) for func, val in zip(types, row)]
                if has_headers:
                    # Make a dictionary
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print("Row", rowno, ": Couldn't convert", row)
                    print("Row", rowno, ":", e)
        
    return records
'''

# Exercise 3.17: From filenames to file-like objects
'''
import csv

def parse_csv(lines, select = None, types = None, has_headers = True, delimiter = ",", silence_errors = False):
    'Parse a lines into a list of records'
    # Raise exception if both the select and the has_headers=False arguments are passed
    if select and (not has_headers):
        raise RuntimeError("select argument requires column headers")
    # Raise exception if lines is a str
    if type(lines) is str:
        raise ValueError("Should not pass in a string")
    rows = csv.reader(lines, delimiter = delimiter)
    if has_headers:
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
    for rowno, row in enumerate(rows, 1):
        try:
            if not row: 	# Skip row with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
            if types:
                    row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                # Make a dictionary
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print("Row", rowno, ": Couldn't convert", row)
                print("Row", rowno, ":", e)
        
    return records
'''

# Exercise 8.2: Adding logging to a module

import csv
import logging

log = logging.getLogger(__name__)

def parse_csv(lines, select = None, types = None, has_headers = True, delimiter = ",", silence_errors = False):
    'Parse a lines into a list of records'
    # Raise exception if both the select and the has_headers=False arguments are passed
    if select and (not has_headers):
        raise RuntimeError("select argument requires column headers")
    # Raise exception if lines is a str
    if type(lines) is str:
        raise ValueError("Should not pass in a string")
    rows = csv.reader(lines, delimiter = delimiter)
    if has_headers:
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
    for rowno, row in enumerate(rows, 1):
        try:
            if not row: 	# Skip row with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
            if types:
                    row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                # Make a dictionary
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                log.warning("Row %d: Couldn't convert %s", rowno, row)
                log.debug("Row %d: %a", rowno, e)
        
    return records
