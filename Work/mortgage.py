# mortgage.py
#
# Exercise 1.7
'''
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid +  payment
print('Total paid', total_paid)
'''

'''
# Exercise 1.8
principal = 500000.0
rate = 0.05
payment = 3684.11
total_paid = 0.0
month = 0

while principal > 0:
    if month >= 12:
        payment = 2684.11
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid +  payment
    month = month + 1
print('Total paid', total_paid)
print('Months taken', month)
'''

'''
# Exercise 1.9
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid +  payment
    month = month + 1
print('Total paid', total_paid)
print('Months taken', month - 1)
'''

'''
# Exercise 1.10
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid +  payment
    print(month, round(total_paid, 2), round(principal, 2))
    month = month + 1
print('Total paid', round(total_paid, 2))
print('Months taken', month - 1)
'''

'''
# Exercise 1.11
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid +  payment
    if principal < 0:
        total_paid = total_paid + principal
        principal = principal - principal
    print(month, round(total_paid, 2), round(principal, 2))
    month = month + 1
print('Total paid', round(total_paid, 2))
print('Months taken', month - 1)
'''

# Exercise 1.17
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid +  payment
    if principal < 0:
        total_paid = total_paid + principal
        principal = principal - principal
    print(f"{month:3d} {total_paid:10.2f} {principal:10.2f}")
    month = month + 1
print(f"Total paid {total_paid:10.2f}")
print(f"Months taken {month - 1}")

