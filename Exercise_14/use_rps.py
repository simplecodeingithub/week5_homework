import rock_paper_scissors

# Now we can use the functions directly without triggering play_game(),just call the function from the script name
u_response = rock_paper_scissors.get_user_choice()
print(f"The user choice is {u_response}")

c_response = rock_paper_scissors.get_computer_choice()
print(f"The computer choice is {c_response}")

result = rock_paper_scissors.determine_winner(u_response,c_response)
print(result)

