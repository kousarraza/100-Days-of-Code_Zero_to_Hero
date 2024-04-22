# 31.	Write a Python program to input length in centimeter and convert it to meter and kilometer.

cm=int(input("Enter length in centimeter : "))

m=cm/100 # 100cm=1 m
km=cm/10000 # 1km=1000m      
print("Distance in meters: ",m)
print("Distance in kilometers: ",km)