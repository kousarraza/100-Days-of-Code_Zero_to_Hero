# 102.Write a program that prompts the user to input an integer and then outputs the number with the digits reversed.
reverse=0
digit=0
num=int(input("Enter a Number: "))
while(num!=0):
    digit=num%10
    reverse =reverse * 10 + digit
    num //= 10
print("Reverse ",reverse)
