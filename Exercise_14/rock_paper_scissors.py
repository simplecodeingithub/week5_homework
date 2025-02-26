import random     # Import the random module to generate random numbers

# defining the function
def get_user_choice() :
    """ This function prompts the user to enter their choice of Rock, Paper, or Scissors.
    :return: str Represents the user's choice as a string, either "Rock", "Paper", or "Scissors"."""
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}  # Dictionary to map user input
    user_input = input("Please Enter your Choice(R,P or S) R for Rock, P for Paper, or S for Scissors:\n").upper()
    if user_input in choices:      # user_input = 'R'
        user_response = choices[user_input]  # choices[R] is 'Rock', because 'R' maps to 'Rock' in choices.
        return user_response      # This returns the valid choice, e.g., "Rock"
    else:
        print("Invalid choice! Please enter R,P or S.")
        return get_user_choice()      # This calls the function again to ask the user for input again
    # The return statement returns an object of the type based on the expression's

def get_computer_choice():
    """This function randomly selects a choice for the computer: Rock, Paper, or Scissors.
     :return: str Represents the computer's choice as a string, either "Rock", "Paper", or "Scissors"."""
    choices = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}   # Dictionary to map numbers to choices
    random_number = random.randint(0, 2)  # Generate a random number between 0 and 2
    comp_response = choices[random_number]
    return comp_response   # Return the value back to the user

def determine_winner(user, computer):
    """This function compares the user's and computer's choices to determine the winner.
     :param1 user: str Represents the user's choice ("Rock", "Paper", or "Scissors").
     :param2 computer: str Represents the computer's choice ("Rock", "Paper", or "Scissors").
     :return: str The result of the game ("You win!", "You lose!", or "It's a draw!")."""
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
        return "YOU LOSE!"


def play_game():
    ####### Main function ########
    """The main entry point of the program where the game logic is executed.
    Plays a complete game of Rock, Paper, Scissors between the user and the computer.
    :return: None This function does not return any value."""
    print("*" * 80)
    print("~~~ Welcome to the Game of Rock, Paper, Scissors! Let's Start the Game. ~~~")
    user_choice= get_user_choice()
    comp_choice = get_computer_choice()

    print(f"\nThe user choice is : {user_choice}")      # Display user choice
    print(f"The Computer choice is : {comp_choice}")  # Display computer choice
    print("~" * 50)

    result = determine_winner(user_choice,comp_choice)  # Determine the winner
    print(f"The result is : {result} ")
    print("~" * 50)

# This block will only run when rock_paper_scissors.py is executed directly,not when imported.
# It prevents the game logic from running automatically when the script is imported into another program.
if __name__ == "__main__":
   play_game()


