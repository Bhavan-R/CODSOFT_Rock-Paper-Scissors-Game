import random

print("========== ROCK PAPER SCISSORS GAME ==========")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:

    # User Input
    user_choice = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    # Computer Choice
    computer_choice = random.choice(choices)

    # Display Choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    # Score Display
    print("\n========== SCORE BOARD ==========")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")

    # Play Again Option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        break

print("\n========== GAME OVER ==========")