import random

# functions go at the top of the code before routine
# if a yes no question is been answered it will follow this def
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "Yes"
            return response

        elif response == "no" or response == "n":
            response = "No"
            return response
        # if the say no, output  'display instructions'
        else:
            print("Please answer yes / no")

# instruction for the game if asked for
def instructions():
    print("******How To Play******")
    print("")
    print("Ever since you were young, you have loved the game ‘Rock / Paper / Scissors’\n"
          "The rules are simple…\n"
          "You get to chose between Rock,Paper or Scissors\n"
          "● Rock beats Scissors\n"
          "● Scissors beats Paper\n"
          "● Paper beats Rock\n" 
          "Your choice will be compared between the computer's choice\n"
          "If you win, you'll get a point. That will be added to your total points\n"
          "If the computer wins, The computer will get point. That will be added to the computer's total points\n"
          "To choose 'Rock', type Rock[R].\n"
          "To choose 'Paper', type Paper[P].\n"
          "To choose 'Scissors', type Scissors[S].\n")
    print("")
    return ""

# users choice between rock paper and scissors
def user_choice(question1):

    valid = False
    while not valid:

        # asks the user for their choice
        response = input(question1).lower()

        # if the user chooses rock or r response equals to Rock
        if response == "rock" or response == "r":
            response = "Rock"
            return response

        # if the user chooses paper or p response equals to paper
        elif response == "paper" or response == "p":
            response = "Paper"
            return response

        # if the user chooses scissors or s response equals to Scissors
        elif response == "scissors" or response == "s":
            response = "Scissors"
            return response

        elif response == "xxx":
            response = "xxx"
            return response

        # if the user chooses anything other than the options listed above it will print
        else:
            print("Please choose between Rock[R],Paper[P] or Scissors[S]")

# if the user inputs using letter it will print an error message
def rounds1(question):
    valid = False
    while not valid:

        response = input(question)

        if response.isalpha() is False and 0 <= int(response) <= 30:
            return response
        elif response.isalpha() is True:
            print("Type using Numbers!")
        elif int(response) <= 0:
            print("Please choose 0 or higher")
        elif int(response) >= 30:
            print("Please choose 30 or lower")
        else:
            ""

def win_by1(question):
    valid = False
    while not valid:

        response = input(question)

        if response.isalpha() is False and 1 <= int(response) <= 30:
            return response
        elif response.isalpha() is True:
            print("Type using Numbers!")
        elif int(response) <= 0:
            print("Please choose 0 or higher")
        elif int(response) >= 30:
            print("Please choose 30 or lower")
        else:
            ""
# main routine goes here


comp_score = 0  # computers points
user_score = 0  # users points
tied = 0  # number of ties

# this is for the users/computers choice and it will write it down in order
comp_picks_list = []
user_picks_list = []

played_before = yes_no("Have you played the game before?  ")
print("You chose {}".format(played_before))

if played_before == "No":
    instructions()

# asks the user how many times they want to play
rounds = rounds1("How many rounds would you like to play, Enter 0 to for infinite play:\n"
                 "Please type using Numbers!\n"
                 ":  ")
r = 0
i = 0
if int(rounds) == 0:
    print("You are in Infinite mode")
# asks the user if they want to see their game history at the end
game_history = yes_no("Would you like to see your Game History at the end of the game?  ")

# if the user wants to play infinite mode it will follow this loop until the user exits
if int(rounds) == 0:
    while i == 0:
        r += 1
        options = ["Rock", "Paper", "Scissors", "Rock", "Paper", "Scissors"]
        comp_pick = random.choice(options)
        print("Enter 'xxx' to exit.")
        user_pick = user_choice("Choose what you want to play with?\n"
                                "Rock[R]\n"
                                "Paper[P]\n"
                                "Scissors[S]\n"
                                ":")
        # if user enters "xxx" it will also break the loop and print Game over
        if user_pick == "xxx":
            print("---Game Over!---")
            break

        print("******Round #{}******".format(r))
        # if user's pick is same as comp's pick it will tie
        if user_pick == comp_pick:
            print("Both selected {}. It's a Tie!".format(user_pick))
            tied += 1
        # if user's pick is rock and comp's pick is scissors user will gain a point
        elif user_pick == "Rock":
            if comp_pick == "Scissors":
                print("Rock smashes Scissors! You Win!")
                user_score += 1
            # but if comp's pick is paper comp will gain a point
            else:
                print("Paper covers Rock! You Lose.")
                comp_score += 1
        # if user's pick is paper and comp's pick is rock user will gain a point
        elif user_pick == "Paper":
            if comp_pick == "Rock":
                print("Paper covers Rock! You Win!")
                user_score += 1
            # but if comp's pick is scissors comp will gain a point
            else:
                print("Scissors cuts Paper! You Lose.")
                comp_score += 1
        # if user's pick is scissors and comp's pick is paper user will gain a point
        elif user_pick == "Scissors":
            if comp_pick == "Paper":
                print("Scissors cuts Paper! You Win!")
                user_score += 1
                # but if comp's pick is rock comp will gain a point
            else:
                print("Rock smashes Scissors! You Lose.")
                comp_score += 1

        # it will print these at the end of each round
        comp_picks_list.append(comp_pick)
        user_picks_list.append(user_pick)
        print("You: {}".format(user_pick))
        print("Computer: {}".format(comp_pick))
        print("Player Wins:{}".format(user_score))
        print("Computer Wins:{}".format(comp_score))
        print("******Match History******")
        print("User list:", user_picks_list)
        print("Computer list:", comp_picks_list)
        print("----------------------------------------------")

# else it will follow this loop until it broken
else:
    # asks the user how many rounds they want to win by
    win_by = win_by1("How many points would you like to win by?  ")
    while r <= int(rounds):
        r += 1
        options = ["Rock", "Paper", "Scissors", "Rock", "Paper", "Scissors"]
        comp_pick = random.choice(options)
        user_pick = user_choice("Choose what you want to play with?\n"
                                "Rock[R]\n"
                                "Paper[P]\n"
                                "Scissors[S]\n"
                                ":")
        if user_pick == "xxx":
            break
        print("******Round #{}******".format(r))
        # if user's pick is same as comp's pick it will tie
        if user_pick == comp_pick:
            print("Both selected {}. It's a Tie!".format(user_pick))
            tied += 1
        # if user's pick is rock and comp's pick is scissors user will gain a point
        elif user_pick == "Rock":
            if comp_pick == "Scissors":
                print("Rock smashes Scissors! You Win!")
                user_score += 1
            # but if comp's pick is paper comp will gain a point
            else:
                print("Paper covers Rock! You Lose.")
                comp_score += 1
        # if user's pick is paper and comp's pick is rock user will gain a point
        elif user_pick == "Paper":
            if comp_pick == "Rock":
                print("Paper covers Rock! You Win!")
                user_score += 1
            # but if comp's pick is scissors comp will gain a point
            else:
                print("Scissors cuts Paper! You Lose.")
                comp_score += 1
        # if user's pick is scissors and comp's pick is paper user will gain a point
        elif user_pick == "Scissors":
            if comp_pick == "Paper":
                print("Scissors cuts Paper! You Win!")
                user_score += 1
            # but if comp's pick is rock comp will gain a point
            else:
                print("Rock smashes Scissors! You Lose.")
                comp_score += 1

        # it will print these at the end of each round
        comp_picks_list.append(comp_pick)
        user_picks_list.append(user_pick)
        print("You: {}".format(user_pick))
        print("Computer: {}".format(comp_pick))
        print("Player Wins:{}".format(user_score))
        print("Computer Wins:{}".format(comp_score))
        print("******Match History******")
        print("User list:", user_picks_list)
        print("Computer list:", comp_picks_list)
        print("----------------------------------------------")

        # if user score or comp score is equals to win by it will break the loop and print Game over
        if user_score == int(win_by) or comp_score == int(win_by):
            print("---Game Over!---")
            break

        # if the number of 'r' is higher than the number of rounds it will break the loop and print Game over
        elif r >= int(rounds):
            print("---Game Over!---")
            break

# if the user points is higher than computers points it will print...
if user_score > comp_score:
    print("******You've Won!******")
    print("******CONGRATULATIONS******")

# if the computer points is higher than the users points it will print...
elif comp_score > user_score:
    print("******You've Lost!******")
    print("******BETTER LUCK NEXT TIME******")

# otherwise it will print this (meaning they have tied)
else:
    print("******You've Tied******")
    print("******BETTER LUCK NEXT TIME******")

# match summary will print after the game finishes
print("------Match Summary------")
print("Player|Computer")
print("Wins: {} | {}".format(user_score, comp_score))
print("Lost: {} | {}".format(comp_score, user_score))
print("tied: {} | {}".format(tied, tied))

# if the user says yes to see their game history it will print
if game_history == "Yes":
    print("******Game History******")
    print("User list:", user_picks_list)
    print("Computer list:", comp_picks_list)

# feedback
having_fun = yes_no("Did you like the Game?  ")
if having_fun == "Yes":
    print("Thank You, for the feedback! :)")
elif having_fun == "No":
    print("Sorry to hear that :(")

print("----------------------Thanks for playing----------------------")
