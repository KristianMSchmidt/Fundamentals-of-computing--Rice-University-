import simplegui

frame_rate=0
def draw_handler(canvas):
    global frame_rate
    frame_rate +=1

    if frame_rate%60==0:
        print time, frame_rate
    if time<16:
        canvas.draw_text('Snake', (150, 100), 50, 'Red')

    if time<15:
        canvas.draw_text('Snake', (150, 100+0.0005*frame_rate**2), 50, 'Red')

    if 10<time<20 and not time%3==0:

        canvas.draw_text('By Kristian 2017', (40, 130), 30, 'Green')
    if 0<time<20:
        canvas.draw_polygon([(10, 20), (20, 30), (30, 10)], 12, 'Green')
        canvas.draw_polygon([[30, 20], [100, 20], [100, 100], [30, 100]], 12, 'Red', "Red")
        canvas.draw_polygon([(50, 70), (80, 40), (30, 90)], 5, 'Blue', 'White')
        canvas.draw_polygon([[90, 70], [80, 40], [70, 90], [70, 70]], 12, 'Yellow', 'Orange')
    if time>16:
        frame.set_canvas_background("White")
        canvas.draw_text('To start game: Press Space', (150, 100), 15, 'Red')
    if time==30:
        frame.stop()
        timer.stop()

def other_handler(canvas):
    canvas.draw_text("Yay! You found me!", (100, 170), 20, "Aqua")
time=0


frame = simplegui.create_frame('Testing', 500, 300)

frame.set_canvas_background("Grey")
frame.start()
frame.set_draw_handler(draw_handler)



def timer_handler():
    global time
    time = time+1
    #print time

   # if time==5:
    #    frame.set_draw_handler(other_handler)
    #if time==9:
     #   timer.stop()




timer = simplegui.create_timer(1000, timer_handler)
timer.start()
