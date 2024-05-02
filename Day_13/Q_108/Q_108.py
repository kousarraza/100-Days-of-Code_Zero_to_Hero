# 108.	Write a Python  program to input a number and check whether the number is Perfect number or not.

num = int(input("Enter a number: "))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum==num):
    print(num," is a perfect number. ")
else:
     print(num," is not  a perfect number. ")