
def new_game():
    global snakes, s1, cheeses
    non_human_snakes=int(0.02*(GRID_SIZE**2))

    lst=[]
    numbers=range(1,GRID_SIZE+1)

    for n in range (1,2*non_human_snakes+1):
        n=random.choice(numbers)
        numbers.remove(n)
        lst.append(n)

    if lst[0]<int(GRID_SIZE/2):
        s1_direction="right"
    elif lst[0]>=int(GRID_SIZE/2):
        s2_direction="left"
    if lst[1]<int(GRID_SIZE/2):
        s1_direction="down"
    elif lst[1]>=int(GRID_SIZE/2):
        s1_direction="up"

    s1=Snake( [(lst[0],lst[1])] ,s1_direction, "Lime")
    snakes=[s1]
    lst.pop(0)
    lst.pop(0)

    for n in range(len(lst)):
        snakes.append(Snake([(lst[n-2],lst[n-1])],random.choice(DIRECTIONS), random.choice(COLOR_LIST), auto=True))


    cheeses=[]
    for n in range(int(0.06*GRID_SIZE**2)):
        cheeses.append(Cheese((n,n)))
    for cheese in cheeses:
        cheese.new_position()

    set_score()
