# pcost.py
#
# Exercise 1.27

total = 0.00
with open("Data/portfolio.csv", "rt") as f:
    headers = next(f)
    for line in f:
        row = line.split(",")
        cost = int(row[1]) * float(row[2][0:-1])
        total = total + cost
print(f"Total cost {total:0.2f}")


# Exercise 1.30

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

# Exercise 1.31: Error handling

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