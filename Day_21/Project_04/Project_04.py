import random
# Define options for the game
choices = ["rock", "paper", "scissors"]
# Get user input
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Check for valid input
if user_choice not in choices:
  print("Invalid choice. Please enter rock, paper, or scissors.")
  exit()

# Generate computer's random choice
computer_choice = random.choice(choices)

# Determine the winner
print("Computer's choice:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")