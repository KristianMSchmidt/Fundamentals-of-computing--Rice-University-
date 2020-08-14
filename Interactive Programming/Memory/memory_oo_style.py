# Add an selection method for Tile class
import random
#################################################
# Student adds code where appropriate

import simplegui

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100

# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc

    # definition of getter for number
    def get_number(self):
        return self.number

    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed

    # expose the tile
    def expose_tile(self):
        self.exposed = True

    # hide the tile
    def hide_tile(self):
        self.exposed = False

    # string method for tiles
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert


# define event handlers

game_state=0
turns=0

def mouseclick(pos):
    global game_state, tile_1, tile_2
    global turns

    for tile in tiles:
        if tile.is_selected(pos):
            if tile.is_exposed():
                pass
            else:
                tile.expose_tile()

                if game_state==0:
                    print "game_state:",game_state
                    tile_1=tile
                    game_state=1
                    print "tile 1:",tile_1
                    print ""

                elif game_state==1:
                    print "game state",game_state
                    tile_2=tile
                    print "tile 1:",tile_1
                    print "tile 2:",tile_2
                    game_state=2
                    turns +=1
                    print "Turns: ", turns
                    print ""
                else:
                    print "game_state", game_state
                    print "tile_1:", tile_1
                    print "tile 2:",tile_2

                    if not tile_1.get_number()==tile_2.get_number():
                         print "nu"
                         tile_1.hide_tile()
                         tile_2.hide_tile()

                    tile_1=tile
                    print "ny tile 1:", tile_1
                    game_state=1
                    print ""


def draw(canvas):
    for tile in tiles:
        tile.draw_tile(canvas)

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 16 * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

#create 8 tiles
x=range(1,9)
y=range(1,9)
x.extend(y)
random.shuffle(x)
print x
print ""
tiles=[]
m=-1
for n in x:
    m=m+1
    tiles.append(Tile(n,False,[m*TILE_WIDTH, TILE_HEIGHT]) )


# get things rolling
frame.start()


###################################################
# Clicking on tile should flip them once
