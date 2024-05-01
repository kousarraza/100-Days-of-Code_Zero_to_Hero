# 100 Write a  Python program that reads a set of integers from user, and then prints the sum of the even and odd integers.
start=int(input("Enter First Number: "))
end=int(input("Enter Last Number: "))
even_sum=0
odd_sum=0
for i in range(start,end+1):
    if(i%2==0):
        even_sum+=i
    else:
        odd_sum+=i
print("Sum of Even Number: ",even_sum,"\nSum of Odd Number",odd_sum)

