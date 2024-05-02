# 113. Write a Python program that asks the user to enter a number and prints the sum of the divisors of that number. The sum of the divisors of a number is an important function in number theory

num = int(input("Enter a number: "))
divisors_sum = 0
for i in range(1, num + 1):
    if num % i == 0:
     divisors_sum += i

# Calculate the sum of divisors and print the result
print("Sum of divisors of", num, "is:", divisors_sum)
