# this is importing the random module for us to use for our R,PS game
import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

def user_input():
    question = input("This is a game of Rock, Paper, Scissors. Which option do you want to choose? Rock 'R', Paper 'P' or Scissors 'S? ").upper()
    rpsdict = {
        'R':rock,
        "P":paper,
        "S":scissors
    }
    rps_choice = rpsdict[question]
    return rps_choice

def computer_input():
    question = random.randint(0,2)
    rpsintegers = {
        0 :rock,
        1: paper,
        2 :scissors
    }
    rps_choice = rpsintegers[question]
    return rps_choice

# # This is where I will be using the random function to

def comparison_of_user_and_computer(computer, user):
    if user == computer:
        print("Its a draw!")

    elif (user == rock and computer == scissors) or (user == paper and computer == rock) or (user == scissors and computer == paper):
        print("YOU WIN!!")

    else:
        print("YOU LOSE!")


player_choice = user_input()
print("You chose: " + player_choice)

computer_choice = computer_input()
print("Computer chose: " + computer_choice)

comparison_of_user_and_computer(computer_choice, player_choice)