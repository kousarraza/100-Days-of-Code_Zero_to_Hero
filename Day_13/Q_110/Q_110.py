# 110. 	Write a program in Python to input a number and check whether the number is prime number or not using for loop.
num = int(input("Enter a number: "))
flag=1  
for i in range(2,num//2):
    if(num%i==0):   
        flag=0   
        break 

if(flag==1 and num>1):
    print(num,"is prime number ")
else:
    print(num,"is not prime number ")