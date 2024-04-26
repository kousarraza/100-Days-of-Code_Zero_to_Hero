# 62. Write a Python program  to swap a number by using diffrent methods.

n1=int(input("Enter 1st  Number: "))
n2=int(input("Enter 2nd  Number: "))

#Swap Numbers Using Temporary Variable
print("Swap Numbers Using Temporary Variable ")

print("Before Swap ")
print("1st Number is: ",n1)
print("2nd Number is: ",n2)
temp=n1
n1=n2
n2=temp
print("After Swap ")
print("1st Number is: ",n1)
print("2nd Number is: ",n2)

#Swap Numbers Without Using Temporary Variables

print("Swap Numbers  by using + and  - operators  ")

print("Before Swap ")
print("1st Number is: ",n1)
print("2nd Number is: ",n2)

n1=n1+n2
n2= n1-n2
n1=n1-n2

print("After Swap ")
print("1st Number is: ",n1)
print("2nd Number is: ",n2)



#Swap Numbers  using + and - Arthemetic Operators and without third Variable

print("Swap Numbers  by using + and  - operators  ")

print("Before Swap ")
print("1st Number is: ",n1)
print("2nd Number is: ",n2)

n1=n1+n2
n2= n1-n2
n1=n1-n2

print("After Swap ")
print("1st Number is: ",n1)
print("2nd Number is: ",n2)

#Swap Numbers  using * and / Arthemetic Operators and without third Variable.

print("Swap Numbers  by using * and  / operators  ")

print("Before Swap ")
print("1st Number is: ",n1)
print("2nd Number is: ",n2)

n1=n1*n2
n2= n1//n2
n1=n1//n2

print("After Swap ")
print("1st Number is: ",n1)
print("2nd Number is: ",n2)


