# functions go up here
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

        # if the user chooses anything other than the options listed above it will print
        else:
            print("Please choose between Rock[R],Paper[P] or Scissors[S]")


# main routine goes here
user_pick = user_choice("Choose what you want to play with?\n"
                    "Rock[R]\n"
                    "Paper[P]\n"
                    "Scissors[S]\n"
                    ":").lower()
