# 84..	Write a Python program to given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.

age = int(input("Enter a person's age: "))
life_stage=0
if (age <= 0):
    life_stage="Invalid Age"
elif (age <= 1):
    life_stage="Baby"
elif (age <= 3):
    life_stage="Toddler"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
elif age <= 12:
    life_stage="Child"
elif age <= 19:
    life_stage="Teenager"
elif age <= 65:
    life_stage="Adult"
else:
    life_stage="Old Codger"
print(f"{age} years old is considered {life_stage}.")