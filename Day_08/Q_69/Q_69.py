# 69.  Write a Python program to find minimum between three numbers.

a=int(input("Enter 1st  Number: "))
b=int(input("Enter 2nd  Number: "))
c=int(input("Enter 3rd  Number: "))
if(a<b and a<c):
     print("Min is:",a)
elif(b<a and b<c):
    print("Min is:",b) 
else:
    print("Min is:",c)  
