show_instructions = ""
while show_instructions.lower() != "xxx":

    # ask the user if they have played before
    show_instructions = input("Have you played this game before?  ").lower()

    # if they say yes, output 'program continues'
    if show_instructions == "yes":
        print("Program continues")

    elif show_instructions == "no":
        print("Display instructions")
    # if the say no, output  'display instructions'
    else:
        print("Please answer yes / no")
