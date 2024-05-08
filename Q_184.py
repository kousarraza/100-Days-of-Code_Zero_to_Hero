# 184. Write a  Python program to iterate over a dictionary.
# Iterating over a dictionary
my_dict = {'apple': 5, 'banana': 3, 'orange': 7}

# Iterating through keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)
