# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random


# helper function to start and restart the game
def new_game(upper_limit_of_range):
    # initialize global variables used in your code here

    global upper_limit
    upper_limit=upper_limit_of_range

    global secret_number
    secret_number=random.randrange(0,upper_limit_of_range)

    global count
    if upper_limit_of_range==100:
        count=7
    else:
        count=10

    print "New game. Range is from 0 to",str(upper_limit_of_range)+"."
    print "You have", count, "guesses in total."
    #print "secret_number is",secret_number
    print ""




# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    new_game(100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    new_game(1000)



def input_guess(guess):
    global count
    try:
        int(secret_number)
    except:
        print "To start new game: Choose Range"
        print ""
        return()
    try:
        guess=int(guess)
    except:
        print "Error: Guess must be an integer"
        print "You have", count, "guesses left"
        return()

    print "Guess was", guess

    count=count-1

    if count==0:
        print "Secret number is", secret_number
        print "Game over!"
        print ""
        print ""
        new_game(upper_limit)
    else:

        if guess==secret_number:
            print "Correct!"
            print ""
            print ""
            new_game(upper_limit)

        elif guess<secret_number:
            print "Higher!"
            print " "
            print "You have", count, "guesses left"

        else:
            print "Lower!"
            print ""
            print "You have", count, "guesses left"

 # create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
frame.add_button("New Game: Range [0,100)", range100,200)
frame.add_button("New Game: Range [0,1000)",range1000,200)
frame.add_input("Enter guess", input_guess, 200)



frame.start()
