# 106. Write a Python program to input a number from user and calculate product of its digits.
num = int(input("Enter a number: "))
product = 1
for digit in str(num):
    product *= int(digit)

print("Product of digits =", product)
