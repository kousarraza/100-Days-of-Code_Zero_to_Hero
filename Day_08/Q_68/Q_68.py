# 68. Write a Python program to find maximum between three numbers.
a=int(input("Enter 1st  Number: "))
b=int(input("Enter 2nd  Number: "))
c=int(input("Enter 3rd  Number: "))
if(a>b and a>c):
     print("Max is:",a)
elif(b>a and b>c):
    print("Max is:",b) 
else:
    print("Max is:",c)  
