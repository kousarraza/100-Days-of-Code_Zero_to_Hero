# 125. Write a Python program to Calculate the sum and average of the digits present in a string.

input_str = "KouSarRaza29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)