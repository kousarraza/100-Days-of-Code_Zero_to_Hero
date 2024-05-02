# 114. Write a  Python program that counts how many of the squares of the numbers from 1 to 100 end in a 4 and how many end in a 9.

count_4 = 0
count_9 = 0
for num in range(1, 101):
    square = num ** 2
    last_digit = square % 10
    if last_digit == 4:
        count_4 += 1
    elif last_digit == 9:
        count_9 += 1

print("Number of squares ending in 4:", count_4)
print("Number of squares ending in 9:", count_9)
