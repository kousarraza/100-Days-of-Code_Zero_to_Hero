# 53.	Write a Python  program to find the third angle of triangle if two angles are given. 

a=int(input("Enter first angle of triangle"))
b=int(input("Enter second angle of triangle"))

# sum of angles of triangle=180'
#a+b+c=180'

c=180-(a+b)
print("Third angle of triangle is: ",c)