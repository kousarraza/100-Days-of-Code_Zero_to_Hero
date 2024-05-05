# 138. Write a Python program to get the smallest number from a list.

list1=[213,4,34,12,9,11]
largest=list1[0]
for i in range(1,len(list1)):
    if list1[i] <largest:
        largest=list1[i]
print(largest)