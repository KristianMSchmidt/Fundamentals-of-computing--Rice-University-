# Simple "screensaver" program.

# Import modules
import simplegui
import random

# Global state
position = [50, 50]
width = 500
height = 500
interval = 200
verbs=[" dislikes", " fucks", " humiliates", " kisses"]
verbs_past=[" disliked", " fucked", " humiliates", "kissed"]
males=["Kristian", "Tom", "Hans", "Trine"]
females=[" Katrine", " Anja", " Sigrid", " Danny Boy"]
message= "Nu starter vi"


counter={}
#counter["anja"]=1
# Handler for text box
def update(text):
    global message
    message = text

# Handler for timer
def tick():
    a=random.randrange(0,200)
    b=random.randrange(50,300)
    position[0]=a
    position[1]=b

    global message
    m = random.randrange(0, 4)
    v = random.randrange(0, 4)
    f = random.randrange(0, 4)

    global counter

    text=males[m]+verbs[v]+females[f]

    try:
        counter[text]= counter[text]+1

    except:
        counter[text]=1


    if m==0 and v==1 and f==1:
        message= "CENSORED!"
        print "CENSORED!::"+text
    else:
        message= text
    #if counter[text] %5==0:
    #print text, ": ",counter[text]

    if counter[text]==20:
        print ""
        for key,val in counter.items():
            print key, val, "times"
        quit()


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")

# Create a frame
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text=frame.add_input("Message:", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

frame.start()
timer.start()
