# 66. Write a Python  program to check whether a number is divisible by 5 and 11 or not.

num=int(input("Enter a Number: "))
if((num%5==0 )and(num%11==0 )):
    print("Divisible by 5 and 11")
else:
    print("not")