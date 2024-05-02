# 111. Write a Python  program to print all uppercase alphabets using while loop.
alphabet = ord('A') 
print("Alphabets from A to Z: ")
while alphabet <= ord('Z'):
    print(chr(alphabet), end=' ')
    alphabet += 1 