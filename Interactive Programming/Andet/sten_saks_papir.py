# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Wrong input"

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below

    if number == 0:
        return "rock"

    elif number == 1:
        return "Spock"

    elif number == 2:
        return "paper"

    elif number ==3:
        return "lizard"

    elif number ==4 :
        return "scissors"

    else:
        return "Wrong input"

    # convert number to a name using if/elif/else
    # don't forget to return the result!


def rpsls(player_choice):
    print("")
    print("Rock, spock, paper, lizard, or scissors!")
    print ("Player chooses: "+player_choice)
    import random
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print("Computer chooses: " +comp_choice)
    #print(player_choice, comp_choice)
    #print(player_number,"  ", comp_number)
    x=(player_number-comp_number)%5
    #print(x)
    if x==0:
        print ("Rematch!")
    elif x==1 or x==2:
        print ("Player wins!")
    else:
        print ( "Computer wins!")
        # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message




# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
