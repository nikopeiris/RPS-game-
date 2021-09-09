# functions go at the top
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        # if the say no, output  'display instructions'
        else:
            print("Please answer yes / no")

def instructions():
    print("******How To Play******")
    print("")
    print("Ever since you were young, you have loved the game ‘Rock / Paper / Scissors’\n"
            "The rules are simple…\n"
            "You get to chose between Rock,Paper or Scissors\n"
            "● Rock beats Scissors\n"
            "● Scissors beats Paper\n"
            "● Paper beats Rock\n" 
            "Your choice will be compaired between the computer's choice\n"
            "If you win, you'll get a point. That will be added to your total points\n"
            "If the computer wins, The computer will get point. That will be added to the computer's total points\n"
            "To choose 'Rock', type Rock.\n"
            "To choose 'Paper', type Paper.\n"
            "To choose 'Scissors', type Scissors.\n")
    print("")
    return ""

# main routine goes here
played_before = yes_no("Have you played this game before?  ").lower()

if played_before == "no":
    instructions()

print("Program continues")

