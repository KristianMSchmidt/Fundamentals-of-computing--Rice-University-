"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random

MAX_REMOVE = 3
TRIALS = 10000

def simulation_game(num_items):
    """
    playing one random game after computers initial move
    num_items is the number of items left after computers initial move

    """
    current_items = num_items

    if current_items<= 0:
        return True

    while True:
        player_move = random.randrange(1,4)
        current_items -= player_move
        if current_items <= 0:
            return False
        comp_move = random.randrange(1,4)
        current_items -= comp_move
        if current_items <= 0:
            return True

def count_wins(num_items):

    """
    determining the number of computers wins out of TRIALS using ramdom_game
    num_items is the number of items left after computers initial move
    """
    computer_wins=0

    for dummy in range(TRIALS):
        if simulation_game(num_items):
            computer_wins +=1

    return computer_wins


def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    returns estimated best computer move give the number of items
    uses count_wins for num_items in range(MAX_REMOVE)+1
    """
    best_move=-1
    biggest_num_wins=-1
    for move in range(1,MAX_REMOVE+1):
        num_wins=count_wins(num_items-move)
        #print move, count_wins(num_items-move), float(count_wins(num_items-move))/float(10000)
        if num_wins>biggest_num_wins:
            biggest_num_wins=num_wins
            best_move=move
    return best_move, float(biggest_num_wins)/float(10000)

def test_evaluate_position():
    for number in range(1,15):
        choice, prob= evaluate_position(number)
        print "Remaning items", number,
        print ",comp. chooses", choice,
        print ", est. prob of succes:", prob

test_evaluate_position()

def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """

    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        #player_move=evaluate_position(current_items)
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

#play_game(12)
