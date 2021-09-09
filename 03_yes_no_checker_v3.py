# functions go at the top of the code before routine
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


# main routine goes here
show_instructions = yes_no("Have you played the game before?  ")
print("You chose {}".format(show_instructions))
print("")
#having_fun = yes_no("Are you having fun?  ")
#print("You said {} to having fun".format(having_fun))