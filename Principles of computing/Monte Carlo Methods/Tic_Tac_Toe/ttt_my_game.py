"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def mc_trial(board, player):
    """
    Plays a random game to the end. Modifies board accoringly.
    Argument player is which player machine player is
    Returns nothing.
    """
    current_player=player
    while board.check_win() is None:
        empty_squares = board.get_empty_squares()
        row, col = random.choice(empty_squares)
        board.move(row,col,current_player)
        current_player = provided.switch_player(current_player)

def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores and a completed board and updates
    the score according to which player is the machine player.
    """
    result = board.check_win()
    dim = board.get_dim()

    if result is None:
        print "Fail. Unfinished game sent to update_score"
        return None

    elif result == 4: # draw
        return

    for row in range(dim):
        for col in range(dim):
            square = board.square(row,col)
            if result == player: #if maschine has won
                if square==player:
                    scores[row][col]+= SCORE_CURRENT
                elif square ==1: #empty
                    continue
                else:
                    scores[row][col] -= SCORE_OTHER
            else:   #machine has lost
                if square == player:
                    scores[row][col] -= SCORE_CURRENT
                elif square ==1: #empty
                    continue
                else:
                    scores[row][col] += SCORE_OTHER

def get_best_move(board,scores):
    """
    Finds all empty squares with max score and return random one them as (row, colon)
    """
    empty_squares = board.get_empty_squares()
    print empty_squares

    if len(empty_squares)==0:
        print "Error: Tried to play full board"
        return

    best_squares=[]
    highest_score=None

    for empty_square in empty_squares:
        row,col=empty_square
        value=scores[row][col]
        #print row,col,value
        if value==highest_score:
            best_squares.append(empty_square)

        elif value>highest_score:
            best_squares=[empty_square]
            highest_score=value
    #print best_squares, highest_score
    return random.choice(best_squares)

def test_get_best_move():
    b1=provided.TTTBoard(3,False,[[1,2,1],[3,2,1],[3,1,1]])
    print b1
    scores=[[-3,6,-2],[8,0,-3],[3,-2,-4]]
    get_best_move(b1,scores)

#test_get_best_move()


def run_a_trial(board, player, scores):
    """
    Runs one mc-trial and updates score accordingly. Doesnt change board
    """
    clone=board.clone()
    mc_trial(clone,player)
    mc_update_scores(scores, clone, player)
    return scores

def run_many_trials(board,player,trials):
    """
    Makes score board. Runs trials number of trials and
    returns final score board
    """
    current_scores=[[0 for dummy in range(board.get_dim())] for dummy in range(board.get_dim())]

    for dummy_number in range(trials):
        current_scores=run_a_trial(board,player,current_scores)

    return current_scores


def mc_move(board,player,trials):
    """
    Returns best move for mashine player (row, col)
    """
    test_scores=run_many_trials(board,player,trials)
    return get_best_move(board,test_scores)


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
