# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

game_has_started=False

# helper function to start and restart the game
def new_game(upper_limit_of_range):
    # initialize global variables used in your code here
    global game_has_started
    game_has_started=True

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

input_line_exists=False

def range100():
    # button that changes the range to [0,100) and starts a new game
    global input_line_exists
    new_game(100)
    if not input_line_exists:
        frame.add_input("Enter guess", input_guess, 200)
        input_line_exists=True


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global input_line_exists
    new_game(1000)
    if not input_line_exists:
        frame.add_input("Enter guess", input_guess, 200)
        input_line_exists=True

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
            print ""
        else:
            print "Lower!"
            print ""
            print "You have", count, "guesses left"
            print ""

# create frame


r_buttons_exist=False

def input_new_game():
    global r_buttons_exist
    if not r_buttons_exist:
        frame.add_button("Range [0,100)", range100,200)
        frame.add_button("Range [0,1000)",range1000,200)
        r_buttons_exist=True
    elif not game_has_started:
        print "To start game: Choose range"
        print ""
    else:
        print "To start new game choose range"
        print ""
        print "Old game continues:"
        print "Range is [0,",upper_limit,")"
        print "You have", count, "guessses left."
        print ""

#register event handlers for control elements and start frame

frame = simplegui.create_frame('Guess the number', 200, 200)
frame.add_button("New Game", input_new_game,200)
#start frame
frame.start()
