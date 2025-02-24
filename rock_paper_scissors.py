# this is importing the random module for us to use for our R,P, S game
import random

# I had created these variables so it would be easier to capitalise later on within the dictionaries
# created a variable for each component of the game and assigned it to a string
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

# def is used to help define the new function
# user_input is the name of the new function and you can see it's a function because it has the brackets (parentheses)
# the colon at the end is essential to keep the syntax of the new function
# defined a new variable called question
# used the input function to ask the user which option they wish to choose
# created a dictionary to store the rock paper scissors options that the user can pick
# The keys represent the option the user can choose 'R, P & S'
# the values represent what each letter stands for.
# squiggly brackets are essential to the syntax of a dictionary to store the values.
# defined a new variable called rps_choice which allows the computer to link the answer from the question variable to the dictionary
# return marks the end of the user_input() function and knows to return the rps choice
def user_input():
    question = input("This is a game of Rock, Paper, Scissors. Which option do you want to choose? Rock 'R', Paper 'P' or Scissors 'S? ").upper()
    rpsdict = {
        "R":rock,
        "P":paper,
        "S":scissors
    }
    rps_choice = rpsdict[question]
    return rps_choice

# def starts to define the new function
# computer_input() is the name of the new function
# brackets and the colon keep the new function syntax
# created a new variable called question
# then I used the random module to import a random method
# The random method used is .randint() and this will pick out a random integer between 0 and 2
# created a dictionary to assign the integers used within the randint function to be assigned to either r, p or s
# The key is the integer and the value is either rock paper or scissors
# squiggly brackets are important for the syntax of the dictionary
# created a new variable called rps_choice and this links the randint method to the dictionary of values
# return allows us to complete the function and knows to return the value of the question
def computer_input():
    question = random.randint(0,2)
    rpsintegers = {
        0 :rock,
        1: paper,
        2 :scissors
    }
    rps_choice = rpsintegers[question]
    return rps_choice

# indentations means it is inside the created function
# first 3 speech marks of docstring need to be indented
# double "=" means equal to - on line 63, this means if computer and user input is the same then it will print 'its a draw"
def comparison_of_user_and_computer(computer, user):
    """

this function is used to compare the computer function and the user input
def is to define the function and we had to name the arguments/parameters within the parentheses
used conditional statements to compare the user_input function and the computer_input function

"""
    if user == computer:
        # print has to be further indented to still be within these parameters
        print("Its a draw")

    # used an else/if statement to state the winning variables
    # if the user had picked rock and the computer had the option scissors then they would win
    # Had to put brackets in between each variables for the computer to read then as separate conditions
    # 'or' also helped to separate the conditions
    # If any of these conditions are met, then it will print out 'YOU WIN!'
    elif (user == rock and computer == scissors) or (user == paper and computer == rock) or (user == scissors and computer == paper):
        print("YOU WIN!!")
    # If there is no draw, or none of the winning conditions have been met, then it will print off you lose.
    # This means that the computer choice would beat the user choice
    else:
        print("YOU LOSE!")

# no indentations means we are now outside of the previous function
# defined a new variable called player_choice and then assigned this to the user_input variable
# the user_input function will go through an iteration and this iteration will be the value of player choice
# at the end, it will print the player choice
player_choice = user_input()
print("You chose: " + player_choice)

# same as the comments above but this will help to show the computer value
computer_choice = computer_input()
print("Computer chose: " + computer_choice)

# calls the comparison function and then prints out the results of the comparison between user and computer
comparison_of_user_and_computer(computer_choice, player_choice)