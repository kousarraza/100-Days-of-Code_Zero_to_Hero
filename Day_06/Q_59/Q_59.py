# 59. Write a Python to read an amount (integer value) and break the amount into the smallest possible number of bank notes.
# Note: The possible banknotes are 1000, 500, 100, 50,20,10, 5, 2 and 1.

amount=int(input("Enter a amount: "))

notes_1000=(amount//1000)
print(notes_1000," Notes of Rs. 1000 ")
notes_500=(amount%1000)//500
print(notes_500," Notes of Rs. 500 ")
notes_100=(amount%500)//100
print(notes_100," Notes of Rs. 100 ")
notes_50=(amount%100)//50
print(notes_50," Notes of Rs. 50 ")
notes_20=(amount%50)//20
print(notes_20," Notes of Rs. 20 ")
notes_10=(amount%20)//10
print(notes_10," Notes of Rs. 10 ")
notes_5=(amount%10)//5
print(notes_5," Notes of Rs. 5 ")
notes_2=(amount%5)//2
print(notes_2," Notes of Rs. 2 ")
notes_1=(amount%2)//1
print(notes_1," Notes of Rs. 1 ") 

