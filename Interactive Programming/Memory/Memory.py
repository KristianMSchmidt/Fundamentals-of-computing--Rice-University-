# implementation of card game - Memory

import simplegui
import random

#global variables
NUMBER_OF_DIFFERENT_CARDS=8
WIDTH_OF_CARD=50
HEIGHT_OF_CARD=100


# helper function to initialize globals
def new_game():
    global cards
    global game_state
    global kort1, kort2, nummer1, nummer2
    global expose
    global turns
    turns=0
    label.set_text("Turns =0")

    expose=[]
    cards=[]
    game_state=0

    for n in range(NUMBER_OF_DIFFERENT_CARDS):
        cards.append(n+1)
        cards.append(n+1)

    random.shuffle(cards)

    print cards


# define event handlers

def mouseclick(pos):
    global game_state
    global turns,kort1,nummer1,kort2,nummer2

    chosen_number=pos[0]//50
    chosen=cards[chosen_number]


    if chosen_number in expose:
        pass

    else:
        if chosen_number not in expose:
            expose.append(chosen_number)
            turns+=1
            if turns%2==0:
                label.set_text("Turns ="+str(turns/2))

        if game_state==0:
            nummer1=chosen_number
            kort1=chosen
            game_state=1

        elif game_state==1:
            kort2=chosen
            nummer2=chosen_number
            game_state=2

        else:
            if not kort1==kort2:

                expose.remove(nummer1)
                expose.remove(nummer2)

            nummer1=chosen_number
            kort1=chosen
            game_state=1


# cards are logically 50x100 pixels in size
def draw(canvas):

    #draw cards
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        canvas.draw_text(str(cards[card_index])+" ", [card_pos+12, 69],60, "White")

    #draw green
    for n in range(17):
        if n not in expose:
            canvas.draw_polygon([(n*50,0),((n+1)*50,0),((n+1)*50,100),(n*50,100)],4,"Orange", "Green")

    canvas.draw_line((0,0),(800,0),4,"Orange")
    canvas.draw_line((0,100),(800,100),4,"Orange")
    canvas.draw_line((0,0),(0,100),4,"Orange")
    canvas.draw_line((800,0),(800,100),4,"Orange")

    if len(expose)==16:
        frame.set_draw_handler(draw2)

t2=0
def draw2(canvas):
    global t2
    t2 +=1
    frame.set_canvas_background('Grey')
    canvas.draw_text("Du har vundet. Antal traek: "+str(turns/2),(30, 60),40, "Green")
    if t2==120:
        frame.set_draw_handler(draw)
        new_game()


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()
