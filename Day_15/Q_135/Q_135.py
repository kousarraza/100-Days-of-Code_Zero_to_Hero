# 135. 	Write a Python program to find the average of elements in a list.
list1=[2,4,6]
avg=0
for i in list1:
    avg+=i
l=len(list1)
avg=avg//l
print(avg)