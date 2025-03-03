# Simple "screensaver" program.

# Import modules
import simplegui
import random

# Global state
message = "Python is Fun!"
position = [50, 50]
width = 500
height = 500
interval = 1000

# Handler for text box
def update(text):
    global message
    message = text

#Handler for text box2
def update_speed(number):
    global interval
    interval = int(number)
    timer2=simplegui.create_timer(interval, tick)
    timer2.start()

# Handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")

# Create a frame
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text=frame.add_input("Message:", update, 150)
speed=frame.add_input("Milisecs:",update_speed,150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()
timer.start()
