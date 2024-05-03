# 123 Write a  Python program to count the number of vowels  in a given string.

str1=input("Enter a String: ")
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in str1:
    if char in vowels:
      vowel_count += 1
print(f"The number of vowels in '{str1}' is: {vowel_count}")