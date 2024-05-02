# 103. 	Write a Python program to print all alphabets from a to z using while loop.
alphabet = ord('a')  # ASCII value of 'a'
print("Alphabets from a to z:")
while alphabet <= ord('z'):
    print(chr(alphabet), end=' ')  # Print the current alphabet
    alphabet += 1  # Move to the next alphabet by incrementing ASCII value

