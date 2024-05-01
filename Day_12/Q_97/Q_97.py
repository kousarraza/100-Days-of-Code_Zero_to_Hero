# 97. Write a  Python program to find the factorial value of any number entered through the keyboard.
num = int(input("Enter the number: "))
fact=1
for i in range(1,num+1):
    fact*=i
print("The factorial of", num, "is", fact)
