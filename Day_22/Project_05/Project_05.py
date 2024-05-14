from random import randint
# Generate a random number between 1 and 100 (inclusive)
secret_num = randint(1,100)

# Initialize turns and guess variables
num_guesses = 0
guess = 0
# Game loop 
while guess != secret_num and num_guesses <= 4:

    # Ask the question
    guess = eval(input('Enter your guess (1-100): '))
    # Check guess
    num_guesses = num_guesses + 1
    if guess < secret_num:
        print('HIGHER.', 5-num_guesses, 'guesses left.\n')
    elif guess > secret_num:
        print('LOWER.', 5-num_guesses, 'guesses left.\n')
    else:
         print('You got it!')
 #  check the answer 
if num_guesses==5 and guess != secret_num:
    print('You lose. The correct number is', secret_num)