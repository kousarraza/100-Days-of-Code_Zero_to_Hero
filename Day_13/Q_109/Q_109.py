# 109. Write a Python  program to input a number from user and check whether given number is Armstrong number or not. 

num = int(input("Enter a number: "))
temp=num
sum=0
while(num>0):
    r=num%10    
    sum= sum+(r*r*r)    
    num=num//10 
if(temp==sum):    
    print(temp,"is an Armstrong number")  
else:    
    print(temp, "is not an Armstrong number")
   