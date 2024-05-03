# 118. Write a Python  program to create a new string made of the middle three characters of an input string.

str1="Islamabad"
print("Original String is", str1)
mi = int(len(str1) / 2)
res = str1[mi - 1:mi + 2]
print("Middle three chars are:", res)
