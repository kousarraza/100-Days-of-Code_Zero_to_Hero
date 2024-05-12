
# Chose a option 
operation = input('''
Please  select operation you would like to complete:
1 for Addition
2 for Subtraction
3 for Multiplication
4 for Division
5 for Floor Division
6 for Modulus 
7 for Exponentiation 
Enter the number corresponding to the operation: ''')

# Input two numbers from the user
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

# perform addition 
if operation == '1':
    print('{} + {} = '.format(number_1, number_2),(number_1+number_2))
    

elif operation == '2':
    print('{} - {} = '.format(number_1, number_2),(number_1 - number_2))

elif operation == '3':
    print('{} * {} = '.format(number_1, number_2),(number_1 * number_2))

elif operation == '4':
    print('{} / {} = '.format(number_1, number_2),(number_1 / number_2))
elif operation == '5:
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        print('{} // {} = '.format(number_1, number_2),(number_1 // number_2))

elif operation == '6:
    if num2 == 0:
        print("Error! Modulus by zero is not allowed.")
    else:
        print('{} % {} = '.format(number_1, number_2),(number_1 % number_2))
elif operation == '7':
    print('{} ** {} = '.format(number_1, number_2),(number_1 ** number_2))

else:
    print('You have not typed a valid operator, please run the program again.')