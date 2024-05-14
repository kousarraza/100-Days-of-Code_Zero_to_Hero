import random
#Function to generate random numbers
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

print("Welcome to the Multiplication Game!\n")

correct_answers = 0
#game loop
for i in range(1,11):
    #call the function
    num1, num2 = generate_question()
    # Ask the question
    answer = int(input(f"Question {i}: {num1} * {num2} = "))

  #  check the answer
    if answer == num1 * num2:
         print("Correct!")
          # Update score
         correct_answers += 1
    else:
            print(f"Wrong. The answer is {num1 * num2}")
# Print final results
print(f"You got {correct_answers} out of 10 questions correct.")

