# 93.  Write a python to print the multiplication table for a given number entered by the user:
num = int(input("Enter the number for multiplication table: "))

print("Multiplication Table for", num)
print("----------------------------------------")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

