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
    print("Ever since you were small, you have loved the game ‘Rock / Paper / Scissors’ and you have decided"
"to create a custom version of this game. The rules are simple…"
"● Rock beats scissors"
"● Scissors beats paper"
"● Paper beats rock"
"Your game should allow users to play ‘Rock / Paper / Scissors’ against the computer. Below is a list"
"of features that you need to implement (you can add to this list if you’d like)."
"● During the session, the user enters their choice of rock / paper / scissors and it is compared"
"with the computer’s (randomly generated) choice"
"● Round and score mechanics need to be implemented."
"o Users should be able to choose how many rounds they wish to play. They should be"
"able to choose an ‘infinite play’ mode where they type an exit code to quit rather"
"than playing a pre-determined number of rounds."
"o Score could be based on how many rounds have been won / lost / drawn"
"o Games could be set up so that the winner is the first to win ‘x’ number of games"
"where ‘x’ is chosen by the user at the start of the game."

"● End Game features"
"o Allow users to see their game history (users should be able to choose whether or not"
"to see this)"
"o Display game stats (eg: # of games won, lost and tied)")
    print("")
    return ""

# main routine goes here
played_before = yes_no("Have you played this game before?  ").lower()

if played_before == "no":
    instructions()

print("Program continues")