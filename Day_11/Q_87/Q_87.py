# 87 Write a Python program to ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in. Your program should convert the temperature to the other unit. The conversions

temperature=float(input("Enter the temperature: "))

print("Select  Temperature unit:")
print(" F for  Fahrenheit and C for Celsius")

temp=input()
if temp=='F':
    F=9/5*(temperature+32)
    print(" Fahrenheit is: ",F)
elif (temp=='C'):
    C=5/9*(temperature-32)
    print(" Celsius is: ",C)
else:
    print("Invalid Temperature")