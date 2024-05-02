# 104.Write a Python program to input a number from user and count number of digits in the given integer using loop.
count=0
num=int(input("Enter a Number: "))
while(num!=0):
    num//=10
    count+=1
print("Total Digits:",count)
