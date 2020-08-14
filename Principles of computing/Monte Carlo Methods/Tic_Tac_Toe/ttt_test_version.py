"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def mc_trials(board,player):
    """
    Plays a random game to the end. Modifies board accoringly.
    Argument player is which player machine player is
    Returns nothing.
    """
    current_player=player
    while board.check_win() == None:
        empty_squares=board.get_empty_squares()
        row, col =random.choice(empty_squares)
        board.move(row,col,current_player)
        #print board
        current_player=provided.switch_player(current_player)

def mc_update_scores(scores,board,player):
    """
    Takes a grid of scores and a completed board and updates
    the score according to which player is the machine player.
    """
    result=board.check_win()
    #print "maschine player is", player
    #print "result is:", result
    dim=board.get_dim()

    if result==None:
        print "Fail. Unfinished game sent to update_score"
        quit()
    elif result == 4: # draw
    #    print "draw"
        return None

    for row in range(dim):
        for col in range(dim):
            square=board.square(row,col)
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
    empty_squares=board.get_empty_squares()
    if len(empty_squares)==0:
        print "Error: Tried to play full board"
        return None
    #print "alle empty", empty_squares
    best_squares=[]
    highest_score=-1

    for empty_square in empty_squares:
        row,col=empty_square
        value=scores[row][col]
        #print empty_square, value
        if value==highest_score:
            best_squares.append(empty_square)
        elif value>highest_score:
            best_squares=[empty_square]
            highest_score=value
        #print empty_square, empty_square
    #print "best empty square", best_squares
    return random.choice(best_squares)

def test2():
    b1=provided.TTTBoard(3)
    #mc_trials(b1,2)
    b1.move(0,1,2)
    b1.move(1,1,3)
    b1.move(2,2,3)
    print b1
    scores =[[dummy for dummy in range(b1.get_dim())] for dummy in range(b1.get_dim())]
    scores [2][0]=12
    scores [1][1]=30
    scores [1][2]=12
    scores [2][1]=222


    print "scores", scores

    #mc_update_scores(scores,b1,2)
    print "choce", get_best_move(b1,scores)
#test2()

def run_a_trial(board, player, scores):
    """
    Runs one mc-trial and updates score accordingly
        """
    clone=board.clone()
    mc_trials(clone,player)
    #print clone
    #print "finished trial game \n", clone
    mc_update_scores(scores, clone, player)
    #print "updates scores", scores
    return scores

def test_run_a_trial():
    b1=provided.TTTBoard(3)

    scores=scores =[[0 for dummy in range(b1.get_dim())] for dummy in range(b1.get_dim())]

    #mc_trials(b1,2)
    b1.move(0,0,2)
    b1.move(1,1,3)
    b1.move(1,0,3)
    print b1
    new_scores= run_a_trial(b1,3,scores) #plaer is =
    print new_scores
    print run_a_trial(b1,3,new_scores)
    print b1
#test_run_a_trial()

def run_many_trials(board,player,trials):
    current_scores=[[0 for dummy in range(board.get_dim())] for dummy in range(board.get_dim())]

    for dummy_number in range(trials):
        current_scores=run_a_trial(board,player,current_scores)
    return current_scores

def test_run_many_trials():
    b1=provided.TTTBoard(3)
    b1.move(1,1,2)
    print b1
    print run_many_trials(b1,3,10)

#test_run_many_trials()



def mc_move(board,player,trials):
    """
    Takes a board, runs trials number of trials with current maschine player set to player.
    Returns best move for mashine player (row, col)
    """
    test_scores=run_many_trials(board,player,trials)
    return get_best_move(board,test_scores)

def test_mc_move():
    b1=provided.TTTBoard(3)
    #b1.move(1,1,2)
    b1.move(0,0,3)
    #b1.move(0,2,3)
    #b1.move(0,1,3)
    b1.move(2,0,2)
    b1.move(2,2,2)
    #b1.move(2,1,2)
    #b1.move(2,2,3)

    print b1

    move=mc_move(b1,3,10000)
    b1.move(move[0],move[1],3)
    print b1

    #move=mc_move(b1,2,10000)
    #b1.move(move[0],move[1],3)
    #print b1


test_mc_move()


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)



"""
Test suites for the game"
"""

import poc_simpletest



def test_suite1():

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    #create boards to test
    b0=provided.TTTBoard(3) #maschineplayer is X
    b0.move(1,1,2)
    print "initialboard \n", b0
    mc_trials(b0,3)
    print "finalboard \n", b0

    #print b0.get_dim()

    scores =[[0 for dummy in range(b0.get_dim())] for dummy in range(b0.get_dim())]
    #scores[0][0]=3
    #scores[1][1]=5
    print "initial scores", scores
    mc_update_scores(scores, b0, 3)
    print "final scores:", scores


    # test the method

    #suite.run_test(mc_trials(b0, provided.PLAYERO), 1, "Test #1:")
    #suite.run_test(b1.is_game_won(), False, "Test #2:")
    #suite.run_test(b2.is_game_won(), False, "Test #3:")
    #suite.run_test(b3.is_game_won(), True, "Test #4:")

    #report test results
    suite.report_results()
#test_suite1()




def test():
    b=provided.TTTBoard(2)
    print b
    print b.get_dim()
    print b.square(0,0)
    print b.get_empty_squares()
    b.move(1,2,provided.PLAYERX)
    print b
    b.move(2,0,3)
    print b
    print b.check_win()
test()
