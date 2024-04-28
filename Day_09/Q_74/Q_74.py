# 74. Write a Python program to check whether a triangle is valid or not if angles are given.

print("Enter Three angles of  triangles: ")
a=int(input())
b=int(input())
c=int(input())

if((a+b+c==180 and a> 0) and (b>0 and c>0)):
    print("Triangle is valid ")
else:
    print("Triangle is not valid ")