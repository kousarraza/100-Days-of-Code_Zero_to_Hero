# 107. Write a Python program to input a number from user and find all factors of the given number using for loop. 
num = int(input("Enter a number: "))
print("Factors of",num,"are: ")

for i in range(1,num+1):
    if(num%i==0):
        print(i," ")
