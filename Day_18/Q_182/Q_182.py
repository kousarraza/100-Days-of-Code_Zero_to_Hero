# 182.  Write a  Python program to remove a key from a dictionary.
fruits={"apple":5,"banana":2,"orange":9}

if 'apple' in fruits:
    # If 'a' is in the dictionary, delete the key-value pair with the key 'a'.
    del fruits['apple']

# Print the updated dictionary 'myDict' after deleting the key 'a' (if it existed).
print(fruits)