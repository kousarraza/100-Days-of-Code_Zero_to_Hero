# 189. Create a  Python function that checks if a number is even or odd and returns the result.
def even_odd(num):
    if (num%2==0):
        print("Even Number")
    else:
        print("Odd Number")
num=int(input("Enter a Number: "))
even_odd(num)