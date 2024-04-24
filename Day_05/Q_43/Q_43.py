# 43. Write a Python program to convert days into  months & days.

days=int(input("Enter number of days: "))
months=days//30
remaining_days=days%30
print("Months: ",months)
print("Days: ",remaining_days)