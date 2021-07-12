# bounce.py
#
# Exercise 1.5

# Date: May 25, 2021

height = 100 #meters
count = 0
while count < 10:
	height = height * 3 / 5
	count = count + 1
	print(count, round(height, 4))