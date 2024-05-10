# 192. Write a function called "count_vowels" that takes a string as input and returns the number of vowels (a, e, i, o, u) in that string.
text = input("Enter a string : ")
vowels = ['a','e','i','o','u']
count = []
def count_vowels(text):
    for i in text:
        if i in vowels:
            count.append(i)
    print("Number of vowels in given text are :",len(count))
count_vowels(text)