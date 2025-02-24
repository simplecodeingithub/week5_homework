import random

def get_user_choice():
    """Prompt the user for input and return Rock, Paper, or Scissors."""
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}  # Dictionary to map user input
    user_input = input("Enter R for Rock, P for Paper, or S for Scissors:\n").upper()
    if user_input in choices:
        user_response = choices[user_input]
        return user_response
    else:
        print("Invalid input! Please enter R,P or S.")
        return get_user_choice()

def get_computer_choice():
    """Generate a random number (0,1,2) and return Rock, Paper, or Scissors."""
    choices = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}   # Dictionary to map numbers to choices
    random_number = random.randint(0, 2)  # Generate a random number between 0 and 2
    comp_response = choices[random_number]
    return comp_response   # Return the corresponding choice

def determine_winner(user, computer):
    """Compare user and computer choices to decide the winner."""
    if user == computer:        # If both choices are the same, it's a draw
        return "It's a draw!"

        # Winning conditions based on the rules
    elif (
            (user == "Rock" and computer == "Scissors") or
            (user == "Paper" and computer == "Rock") or
            (user == "Scissors" and computer == "Paper")
        ):
        return "YOU WIN!!"     # User wins
    else:
        return "You lose!"


def play_game():
    ####### Main function ########
    """The main entry point of the program where the game logic is executed."""
    print("Welcome to Rock, Paper, Scissors! Let's Start the Game.")
    user_choice= get_user_choice()
    comp_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")      # Display user choice
    print(f"Computer chose: {comp_choice}")  # Display computer choice

    result = determine_winner(user_choice,comp_choice)  # Determine the winner
    print(result)


play_game()