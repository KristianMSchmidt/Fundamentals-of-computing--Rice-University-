import simplegui
import random

total_ticks = 0
first_click = True


men =["Hans", "Otto"]
women =["Dorthe", "Grethe", "Lone"]
message="Hans boller Dorthe"

# Input handlers
def mande_input_handler(navn):
    global men
    men.append(navn)
    print (men)
    pass

#Draw handler
def draw_handler(canvas):
    #print message
    canvas.draw_text(message, (20, 20), 12, 'Red')

# Timer handler
def tick():
    pass

# Button handler
def click():
    global message
    x=random.randrange(0,len(men))
    y=random.randrange(0,len(women))
    message= men[x]+" boller "+women[y]

    # Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Skab par", click, 200)
timer = simplegui.create_timer(10, tick)
inp = frame.add_input('Tilfoej mandenavn', mande_input_handler, 150)
frame.set_draw_handler(draw_handler)

# Start timer
frame.start()
timer.start()
