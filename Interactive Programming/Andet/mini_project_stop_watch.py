# template for "Stopwatch: The Game"
import simplegui

# define global variables
number_of_games=0
attempts=0
wins=0
time=0
timer_is_on=False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minuts=t//600
    seconds=(t-(minuts*600))//10
    milisecs=t-minuts*600-seconds*10
    if minuts<10:
        minuts_str="0"+str(minuts)
    else:
        minuts_str=str(minuts)
    if seconds<10:
        seconds_str="0"+str(seconds)
    else:
        seconds_str=str(seconds)
    milisecs_str=str(milisecs)
    return(minuts_str+":"+seconds_str+"."+milisecs_str)


# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global timer_is_on
    if not timer_is_on:
        timer.start()
        timer_is_on=True


def stop():
    global wins
    global timer_is_on
    global attempts

    if timer_is_on:
        timer.stop()
        timer_is_on=False
        attempts=attempts+1
        if time%10==0:
            wins=wins+1

def reset():
    global time
    global attempts
    global wins
    time=0
    attempts=0
    wins=0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time+1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (85, 115), 40, 'White')
    canvas.draw_text(str(attempts)+"/"+str(wins),(240,30),30, "Green")

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)


# register event handlers
frame.add_button("Start", start, 150)
frame.add_button("Stop", stop, 150)
frame.add_button("Reset", reset,150)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw_handler)

#start frame
frame.start()
