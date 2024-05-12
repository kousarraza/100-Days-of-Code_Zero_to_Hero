# import random for random numbers
import random
# Create a Empty list
L = []
# Generate a list of 20 random numbers between 1 and 100
for i in range(20):
    (L.append(random.randint(1, 100)))

# Print the list
print("Generated List:",L)

# Sorted the elements of the list
sorted_list = sorted(L)

# Calculate  the product of the elements in the list
product = 1
for a in L:
    product *= a

# Calculate  sum of the elements in the list
Sum =sum(L)

# Find the largest and smallest values in the list
largest=max(L)
smallest=min(L)

# Calculate the average of the elements in the list
Avg= sum(L) / len(L)


# Find the second largest and second smallest entries in the list
second_largest = sorted_list[-2]
second_smallest = sorted_list[1]

# Count the number of even numbers in the list
even_count = sum(1 for num in L if num % 2 == 0)

# Count the number of odd numbers in the list
odd_count = sum(1 for num in L if num % 2 == 1)

# Find the Square of the list
squared_list = [num ** 2 for num in L]

# Find  the Cube of the list 
cubed_list = [num ** 3 for num in L]

# Find the range of the list
range_value = largest - smallest

# Find the median of the list
sorted_numbers = sorted(L)
n = len(sorted_numbers)
if n % 2 == 0:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
else:
    median = sorted_numbers[n // 2]

# Find the mode of the list

count_dict = {}
for num in L:
    count_dict[num] = count_dict.get(num, 0) + 1
mode_count = max(count_dict.values())
mode = [num for num, count in count_dict.items() if count == mode_count]


print("Sorted List:",sorted_list)
print("Squared list:", squared_list)
print("Cubed list:", cubed_list)
print("Sum of the elements in the list:",Sum)
print("Product of the elements in the list:", product)
print("Largest Value:",largest)
print("Smallest Value:",smallest)
print("Second Largest Value:", second_largest)
print("Second Smallest Value:", second_smallest)
print("Number of Even Numbers in the list:", even_count)
print("Number of Odd Numbers in the list:", odd_count)
print("Median of the list:", median)
if len(mode) == len(L):
    print("Mode of the list: No mode, all values are unique")
else:
    print("Mode of the list:", mode)
print("Range:", range_value)