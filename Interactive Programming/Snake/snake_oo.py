
import simplegui
import random

# Define global variables
CELL_SIZE= 40
GRID_SIZE = 10
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT =GRID_SIZE * CELL_SIZE
SPEED=15 #15 er hurtigt #20 er middel #30 er langsomt
COLOR_LIST=["Blue", "Green", "Olive", "Fuchsia", "Grey", "Brown"]
DIRECTIONS=["left", "right", "up", "down"]

def welcome():
    global game_state
    game_state=0
    new_game()


def new_game():
    global snakes, s1, cheeses

    lst=[]
    numbers=range(2,GRID_SIZE)
    for n in range (1,7):
        n=random.choice(numbers)
        numbers.remove(n)
        lst.append(n)

    if lst[0]<5:
        s1_direction="right"
    elif lst[0]>5:
        s2_direction="left"
    if lst[1]<5:
        s1_direction="down"
    elif lst[1]>5:
        s1_direction="up"

    s1=Snake( [(lst[0],lst[1])] ,s1_direction, "Lime")
    s2= Snake([(lst[2],lst[3])],random.choice(DIRECTIONS), "Red",auto=True)
    s3=Snake([(lst[4],lst[5])], random.choice(DIRECTIONS),"Purple", auto=True)
    snakes=[s1,s2,s3]

    cheeses=set()
    for n in range(int(0.06*GRID_SIZE**2)):
        cheeses.add(Cheese((n,n)))
    for cheese in cheeses:
        cheese.new_position()

    set_score()

def comp_mode():
    global s1

    if s1 in snakes:
        snakes.remove(s1)
    else:
        s1= Snake([free_pos()],"right", "Lime")
        snakes.append(s1)


def free_pos():

    avoid=set()

    for snake in snakes:
        for x in snake.body:
            avoid.add(x)

    for cheese in cheeses:
            avoid.add(cheese.pos)

    if len(avoid)==GRID_SIZE**2:
        print "Succes!"
        return()

    while True:
        x=random.randrange(1,GRID_SIZE+1)
        y=random.randrange(1,GRID_SIZE+1)
        if not (x,y) in avoid:
            return (x,y)

class Cheese:
    def __init__(self, pos):
        self.pos=pos

    def __str__(self):
        return "Cheese at pos" +str(self.pos[0]) + str(self.pos[1])

    def new_position(self):
        self.pos=free_pos()


    def draw(self,canvas):
           canvas.draw_circle([(self.pos[0]-0.5)*CELL_SIZE, (self.pos[1]-0.5)*CELL_SIZE], 0.4*CELL_SIZE, 2,"Yellow", "Yellow")


class Snake:

    def __init__(self, body, dir, color, auto=False, score=0, alive=True, time_dead=0):

        self.direction=dir
        self.alive=alive
        self.color=color
        self.body = body
        self.head= (self.body)[-1]
        self.auto=auto
        self.score=score
        self.time_dead=time_dead

    def __str__(self):
        s= "Snake with head (" + str(self.head[0]) + "," + str(self.head[1])+ ") going " +self.direction +". Auto: "+str(self.auto)
        return(s)

    def change_direction(self, dir):
        self.direction=dir

    def new_head(self):

        if self.direction=="right":
            nyt=(self.head[0]+1,self.head[1])
        elif self.direction=="left":
            nyt=(self.head[0]-1,self.head[1])
        elif self.direction=="up":
            nyt=(self.head[0],self.head[1]-1)
        elif self.direction=="down":
            nyt=(self.head[0],self.head[1]+1)
        return nyt

    def has_eaten(self, new_head):  #efter hovedet er opdaterete
        for cheese in cheeses:
            if cheese.pos==new_head:
                cheese.new_position()
                return True
        return False


    def update_body(self):
        new_head=self.new_head()

        if not is_alive(new_head):
            self.alive=False
            self.color="White"

        else:
            self.body.append(new_head)
            self.head=new_head
            if not self.has_eaten(new_head):
                self.body.pop(0)
            else:
                self.score +=1
                set_score()

    def autoplay(self):
        i=self.head[0]
        j=self.head[1]

        if self.direction=="right":
            if not is_alive((i+1,j)):
                if is_alive((i,j-1)):
                    self.direction="up"
                elif is_alive((i,j+1)):
                    self.direction="down"

        elif self.direction=="left":
            if not is_alive((i-1,j)):
                if is_alive((i,j-1)):
                    self.direction="up"
                elif is_alive((i,j+1)):
                    self.direction="down"

        elif self.direction=="down":
            if not is_alive((i,j+1)):
                if is_alive((i-1,j)):
                    self.direction="left"
                elif is_alive((i+1,j)):
                    self.direction="right"

        elif self.direction=="up":
            if not is_alive((i,j-11)):
                if is_alive((i-1,j)):
                    self.direction="left"
                elif is_alive((i+1,j)):
                    self.direction="right"

        self.update_body()

    def play(self):  ##head moves 1 time pr execuation
        global game_state

        if self.alive:
            if self.auto:
                self.autoplay()
            else:
                self.update_body()
        else:
            #laugh_sound.play()
            self.time_dead +=1
            if not self.auto:
                if self.time_dead ==3:
                    snakes.remove(self)
                    game_state=3
            elif self.time_dead==3:
                    snakes.remove(self)
                    baby_head=free_pos()
                    color=random.choice(COLOR_LIST)
                    snakes.append(Snake([(baby_head)],"left",color,auto=True))

    def draw(self,canvas):

        for pos in self.body:
            corners = [((pos[0]-1)*CELL_SIZE, (pos[1]-1)*CELL_SIZE), ((pos[0]-1)*CELL_SIZE, pos[1]*CELL_SIZE),(pos[0]*CELL_SIZE, (pos[1])*CELL_SIZE), (pos[0]*CELL_SIZE, (pos[1]-1)*CELL_SIZE)]   #draw cells:     def __str__(self):
            canvas.draw_polygon(corners,2, "White", self.color)


def is_alive(head):

        for snake in snakes:
            if head in snake.body[1:len(snake.body)]:
                return False
        if not (0<head[0]<=GRID_SIZE and 0<head[1]<=GRID_SIZE): # and  nyt[0]>GRID_SIZE or nyt[1]<1 or nyt[1]>GRID_SIZE:
            return False
        else:
            return True

def set_score():
    global total_snake_score
    total_snake_score=0

    for snake in snakes:
        if snake.auto:
            total_snake_score += snake.score

    lh.set_text("Your score: "+ str(s1.score))
    ls.set_text("Snake score: " + str(total_snake_score))
    lt.set_text("Total score: " + str(total_snake_score+s1.score)+"/"+str(GRID_SIZE**2))


time=1

def draw(canvas):
    global time
    time+=1

    if game_state==0:
        if (time//20)%2==0:
            canvas.draw_text("Snake!", [(11*WIDTH/64), HEIGHT/2], HEIGHT/4, "Green")
        canvas.draw_text("Press space to start", [(3*WIDTH)/16, (5*HEIGHT)/6], HEIGHT/12, "White")

    if game_state==3:
            canvas.draw_text("Game Over!", [(3*WIDTH)/32, HEIGHT/2], HEIGHT/6, "Red")
            canvas.draw_text("Press space for new game", [(1*WIDTH)/16, (5*HEIGHT)/6], HEIGHT/12, "White")

    if game_state==1:
        if time%20==0:
            for snake in snakes:
                snake.play()

        for cheese in cheeses:
            cheese.draw(canvas)

        for snake in snakes:
            if snake.alive:
                snake.draw(canvas)
            elif snake.time_dead<5:
                if (time//5)%2==0:
                    snake.draw(canvas)

        for i in range(GRID_SIZE-1):
            canvas.draw_line([CELL_SIZE+i*CELL_SIZE,0], [CELL_SIZE+i*CELL_SIZE, HEIGHT],2,"White")
        for i in range(GRID_SIZE-1):
            canvas.draw_line([0, CELL_SIZE+i*CELL_SIZE], [WIDTH, CELL_SIZE+i*CELL_SIZE],2,"White")

def keydown(key):
    global game_state

    for snake in snakes:
        if not snake.auto:
            human_snake=snake

    if key == simplegui.KEY_MAP["up"]:
        if not human_snake.direction=="down":
            human_snake.direction="up"
    if key == simplegui.KEY_MAP["down"]:
        if not human_snake.direction=="up":
            human_snake.direction="down"
    if key == simplegui.KEY_MAP["left"]:
        if not human_snake.direction =="right":
            human_snake.direction="left"
    if key == simplegui.KEY_MAP["right"]:
        if not human_snake.direction=="left":
            human_snake.direction="right"
    if key == simplegui.KEY_MAP["space"]:
        if game_state==0:
            game_state=1
        elif game_state==1:
            welcome()
        elif game_state==3:
            new_game()
            game_state=1

    if key == simplegui.KEY_MAP["p"]:
        comp_mode()


#Music
laugh_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Evillaugh.ogg")

#Set frame and handlers
frame = simplegui.create_frame("Snake", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
lh=frame.add_label("Your score: 0")
frame.add_label("", 200)
ls=frame.add_label("Snake score: 0", 200)
frame.add_label("", 200)
lt=frame.add_label("Total score: 0/"+str(GRID_SIZE**2) ,200)

frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("", 200)
frame.add_label("You play green snake (use arrow keys)", 200)
frame.add_label("", 200)
frame.add_label("No human player: Press 'p'", 200)
#frame.add_label("Insert human: Press 'n'", 200)

frame.set_keydown_handler(keydown)


# start frame
frame.start()
  # start frame

welcome()
