# 139. 	Write a Python program to remove duplicates from a list.
list1=[213,4,34,12,9,11,4,12]
final_list = []
for num in list1:
    if num not in final_list:
        final_list.append(num)
print(final_list)