# 112. Write a Python  program to print all lower alphabets using while loop.
alphabet = ord('a') 
print("Alphabets from a to z: ")
while alphabet <= ord('z'):
    print(chr(alphabet), end=' ')
    alphabet += 1 