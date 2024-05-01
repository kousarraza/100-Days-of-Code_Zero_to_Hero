# 99. Write a Python program to display Fibonacci series up to 10 terms.

first=0
second=1
third=0
for i in range(0,10):
    third=first+second
    print(first,end=" ")
    first=second
    second=third
