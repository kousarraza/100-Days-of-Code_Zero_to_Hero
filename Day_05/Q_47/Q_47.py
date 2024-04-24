# 47. 8.	Write a Python program to convert specified days into years,months, weeks and days.

days=int(input("Enter number of days: "))
years=days//365
months=(days%365)//30
week=(days%30)//7
remaining_days=days%7
print("Years: ",years)
print("Months:",months)
print("Weeks: ",week)
print("Days: ",remaining_days)
