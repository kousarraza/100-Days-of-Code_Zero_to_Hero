# 73.  Write a Python program to check whether a character is Uppercase or Lowercase
ch=input("Enter a character: ")
if(ch>='A' and ch<='Z'):
    print(" It is a upercase letter")
elif(ch>='a' and ch<='z'):
    print(" It is a lowercase letter")
else:
    print("It is  not an alphabetic character")