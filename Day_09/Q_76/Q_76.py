# 76. Write a Python program to check whether the triangle is equilateral, isosceles or scalene triangle.

print("Enter the lengths of three sides of the triangle: ")
a=int(input())
b=int(input())
c=int(input())

if(a==b and b==c):
    print("The triangle is an equilateral triangle ")
elif(a==b or a==c or b==c ):
    print("The triangle is an isosceles triangle")
else:
    print("The triangle is a scalene triangle ")