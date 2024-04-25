# Q_61. Write a Python program to calculate compound interest.

p=float(input("Enter  the Principle amount: "))  
r = float(input("Enter the Rate of Interest: ")) 
t = float(input("Enter the Time Period: "))
n = float(input("Enter the Number of times that interest is compounded per unit t:"))
compound_interest=p*((1+r/100)**t-1)
print("Compound interest is: ",compound_interest)
