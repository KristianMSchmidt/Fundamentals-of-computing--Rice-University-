# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import random
import simplegui  ###
# Functions that compute RPSLS

def name_to_number(name):
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
        #print "Wrong input"
        return "Wrong input"


def number_to_name(number):

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
        #print "Wrong input"
        return "Wrong input"

def rpsls(player_choice):
    print("")

    print ("Player chose: "+player_choice)
    import random
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print("Computer chose: " +comp_choice)
    #print "player_number is",player_number
    #print "computer_number is", comp_number
    x=(player_number-comp_number)%5
    if x==0:
        print ("Rematch!")
    elif x==1 or x==2:
        print ("Player wins!")
    else:
        print ( "Computer wins!")


# Handler for input field
def get_guess(guess):
    if not guess in ("rock", "Spock", "paper", "scissors"):
        print "Error. Bad input '"+guess+"' to rpsls"
    else:
        rpsls(guess)


# Create frame and assign callbacks to event handlers
import simplegui

frame = simplegui.create_frame('GUI-based RPSLS', 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")





###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
