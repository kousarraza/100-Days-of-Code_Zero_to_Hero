#39. Write a Python program to convert mintues into  days,hours ,mintues & seconds.

mint=int(input("Enter number of mintues: "))
days=mint//(24 * 60)
remaining_mint=mint%(24 * 60)
hours=remaining_mint//60
mint_remaining=remaining_mint % 60

sec=mint_remaining*60

print("Days: ",days )
print("Hours: ",hours)
print("Mintues: ",mint)
print("Seconds ",sec)