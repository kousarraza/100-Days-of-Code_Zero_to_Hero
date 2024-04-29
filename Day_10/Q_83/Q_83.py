# 83. Write a Python program to input electricity unit charges and calculate total electricity bill according to the given condition:
''' 
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill '''

units=int(input("Enter number of units: "))
bill_amount = 0
if(units<=50):
        bill_amount = units * 0.50
elif(units<=150):
        bill_amount = (50 * 0.50) + ((units - 50) * 0.75)
elif(units<= 250):
        bill_amount = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
       bill_amount = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

surcharge = bill_amount * 0.20
total_bill = bill_amount + surcharge


print("Electricity Bill ")
print("Units Consumed:", units)
print("Bill Amount: Rs.",bill_amount)
print("Surcharge (20%): Rs. ",surcharge) 
print("Total Bill Amount: Rs. ",total_bill)

