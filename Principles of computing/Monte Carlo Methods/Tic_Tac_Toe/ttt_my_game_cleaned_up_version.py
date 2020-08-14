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
def mc_trial(board,player):
    """
    Plays a random game to the end. Modifies board accoringly.
    Argument player is which player machine player is
    Returns nothing.
    """
    current_player=player
    while board.check_win() == None:
        empty_squares = board.get_empty_squares()
        row, col = random.choice(empty_squares)
        board.move(row,col,current_player)
        current_player=provided.switch_player(current_player)

def mc_update_scores(scores,board,player):
    """
    Takes a grid of scores and a completed board and updates
    the score according to which player is the machine player.
    """
    winner=board.check_win()
    dim=board.get_dim()

    #Error message if game not yet decided
    if winner==None:
        print "Fail. Unfinished game sent to update_score"
        return

    #Don't change scores if game ended in a draw
    elif winner == provided.DRAW:
        return

    #Count board score if game is won or lost
    for row in range(dim):
        for col in range(dim):
            square=board.square(row,col)
            if winner == player:
                if square == player:
                    scores[row][col] += SCORE_CURRENT
                elif square == provided.EMPTY:
                    continue
                else:
                    scores[row][col] -= SCORE_OTHER
            else:
                if square == player:
                    scores[row][col] -= SCORE_CURRENT
                elif square ==  provided.EMPTY:
                    continue
                else:
                    scores[row][col] += SCORE_OTHER

def get_best_move(board,scores):
    """
    Finds all empty squares with max score and return random one them as (row, colon)
    """
    empty_squares=board.get_empty_squares()

    if len(empty_squares)==0:
        print "Error: Tried to play full board"
        return

    best_squares=[]
    highest_score=None

    for empty_square in empty_squares:
        row,col=empty_square
        value=scores[row][col]
        if value==highest_score:
            best_squares.append(empty_square)
        elif value>highest_score:
            best_squares=[empty_square]
            highest_score=value
    return random.choice(best_squares)

def run_trials(board,player,trials):
    """
    Makes score board. Runs desireded number of trials and
    returns total score
    """
    scores=[[0 for dummy in range(board.get_dim())] for dummy in range(board.get_dim())]

    for dummy_number in range(trials):
        clone=board.clone()
        mc_trial(clone,player)
        mc_update_scores(scores, clone, player)

    return scores

def mc_move(board,player,trials):
    """
    Returns best move for mashine player (row, col)
    """
    test_scores=run_trials(board,player,trials)
    return get_best_move(board,test_scores)


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
