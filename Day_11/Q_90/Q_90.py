# 90. Write a Python program for type casting.

a=5
b=4.4
c='5'

print(type(a))
print(type(b))
print(type(c))
print("After type casting")
# change int into float then calculate sum
a=float(a)
print(type(a))
print(a+b)

#change float into int then calculate multiply
a=int(a)
print(a*b)

#change int into string 
a=str(a)
print(type(a))

#string  into int
c=int(c)
print(type(c))