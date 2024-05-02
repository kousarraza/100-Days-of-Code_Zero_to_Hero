# 105.Write a Python  program to input a number and calculate sum of digits using for loop.
num = int(input("Enter a number: "))
sum = 0
for digit in str(num):
    sum += int(digit)
print("Sum of digits =", sum)
