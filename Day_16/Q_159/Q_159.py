# 159. Write a Python program to remove an element from a tuple.
t1=("apple","banana","mango","kiwi")
t1=list(t1)
t1.remove("banana")
t1=tuple(t1)
print(t1)