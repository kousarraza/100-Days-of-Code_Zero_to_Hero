# 72. 	Write a Python program to take  input any character and check whether it is alphabet, digit or special character.
ch=input("Enter a character: ")
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print("It is Alphbet")
elif(ch>= '0' and ch<='9'):
    print("It is Digit")
else:
    print(" It is Special character")