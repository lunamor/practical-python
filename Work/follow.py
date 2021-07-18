# follow.py
#
# Exercise 6.5: Monitoring a streaming data source
'''
import os
import time

f = open("Data/stocklog.csv")
f.seek(0, os.SEEK_END)	# Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == "":
        time.sleep(0.1)	# Sleep briefly and retry
        continue
    fields = line.split(",")
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")
'''

# Exercise 6.6: Using a generator to produce data
'''
import os
import time

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)	# Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line == "":
            time.sleep(0.1)	# Sleep briefly and retry
            continue
        yield line

if __name__ == "__main__":
    for line in follow("Data/stocklog.csv"):
        fields = line.split(",")
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")
'''

# Exercise 6.7: Watching your portfolio

import os
import time

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END)	# Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line == "":
            time.sleep(0.1)	# Sleep briefly and retry
            continue
        yield line

if __name__ == "__main__":
    import report
    portfolio = report.read_portfolio("Data/portfolio.csv")
    for line in follow("Data/stocklog.csv"):
        fields = line.split(",")
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")