##################################################
# Student should add code where relevant to the following.

import simplegui

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""

    first_letter = word[0]
    rest_of_word = word[1 : ]

    global p
    if first_letter in "aeoiu":
        p=word+"way"
    else:
        p=rest_of_word+first_letter+"ay"

    return(p)
    # Student should complete function on the next lines.


# Handler for input field
def get_input(x):
    #print "Oprindeligt ord: ",x
    print(pig_latin(x))

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("Skriv ord", get_input, 150)


# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay
