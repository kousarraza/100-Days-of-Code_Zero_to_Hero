# 86. Write a Python program to find maximum  and minimum between four numbers.

a=int(input("Enter 1st  Number: "))
b=int(input("Enter 2nd  Number: "))
c=int(input("Enter 3rd  Number: "))
d=int(input("Enter 4th  Number: "))
if(a>b and a>c and a>d):
    print("Max is:",a)
elif(b>a and b>c and b>d):
     print("Max is:",b) 
elif(c>a and c>b and c>d):
    print("Max is: ",c)
else:
    print("Max is: ",d)
if(a<b and a<c and a<d):
        print("Min is: ",a)
elif(b<a and b<c and b<d):
         print("Min is: ",b)
elif(c<a and c<b and c<d):
        print("Min is: ",c)
else:
    print("Min is: ",d)
