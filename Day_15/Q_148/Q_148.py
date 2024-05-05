#148 Write a Python program to remove all occurrences of a specific item from a list.
list1=["red","blue","green","red","white","green","green","blue","pink"]
element="red"
while element in list1:
    list1.remove(element)
print(list1)