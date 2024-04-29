# 85.Write a Python program to Determine the season based on the month.

month = int(input("Enter a month number (1-12): "))
season=''
if(month in(12,1,2)):
    season="Winter"
elif(month in(3,4)):
    season="Spring"
elif(month in(5,6,7,8,9)):
    season="Summer"
elif(month in(10,11)):
    season="Fall"
else:
    print("Invalid month number. Please enter a value between 1 and 12.")
print(f"{month} falls in {season}.")