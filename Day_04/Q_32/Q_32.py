# 32.	Write a Python program to input length in milimeter and convert it into centimeter,meter and kilometer.

mm=int(input("Enter length in milimeter : "))
cm=mm/10  # 1cm=10mm
m=mm/1000# 100cm=1 m
km=cm/100000 # 1km=1000m 

print("Distance in centimeters: ",cm)    
print("Distance in meters: ",m)
print("Distance in kilometers: ",km)