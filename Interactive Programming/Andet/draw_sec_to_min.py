# Define a function that returns formatted minutes and seconds

###################################################
# Time formatting function
# Student should enter function on the next lines.

import simplegui

def convert_text(minutes,seconds):
    return(str(minutes) +" minutes and "+str(seconds)+" seconds")

#print(convert_text(3,45))

def format_time(sec):
    minu=sec//60
    sec=sec%60
    global tekst
    tekst=convert_text(minu,sec)
    return(tekst)

#print(converter(124))

# Draw handler
def draw(canvas):
    canvas.draw_text(tekst, [45,80], 20, "White")

# Create frame and assign callbacks to event handlers
frame=simplegui.create_frame("X", 300,200)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()


###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds
