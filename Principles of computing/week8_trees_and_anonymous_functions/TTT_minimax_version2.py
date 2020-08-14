
"""
Mini-max Tic-Tac-Toe Player
Kristian M Schmidt
This version also seems to work more or less optimally (if there is a bug, I cant find it)
#I spend a whole day trying to make this version more elegant, but came to the conclusion, that elegance (in terms
of a short and compact code without any repeition, can come at a price that is too high. Simplicity also means, that
you understnad your own code, so that you can write it without bugs)
"""

#import poc_ttt_gui
import poc_ttt_provided as provided
# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).

    Instructions:
    This function takes a current board and which player should move next. The function should use Minimax to return a
     tuple which is a score for the current board and the best move for the player in the form of a (row, column) tuple.
     In situations in which the game is over, you should return a valid score and the move (-1, -1). As (-1, -1) is an
     illegal move, it should only be returned in cases where there is no move that can be made.
    """

    if board.check_win() != None:

        final_result = board.check_win()
        score_of_final_board = SCORES[final_result]
        no_possible_moves_left = (-1,-1)
        return (score_of_final_board, no_possible_moves_left)

    else:

        legal_moves = board.get_empty_squares()
        board_clones = []
        highest_score = - 2
        lowest_score = 2
        best_move = None

        for indx in range(len(legal_moves)):
            investigated_move = legal_moves[indx]
            investigated_move
            copy = board.clone()
            clone = board.clone()
            clone.move(investigated_move[0], investigated_move[1], player)
            next_player = provided.switch_player(player)
            score = mm_move(clone, next_player)[0]
            if player == provided.PLAYERX:
                if score == 1:
                    return (score, investigated_move)
                elif score > highest_score:
                    highest_score = score
                    best_move = investigated_move
            elif player == provided.PLAYERO:
                if score == - 1:
                    return (score, investigated_move)
                elif score < lowest_score:
                    lowest_score = score
                    best_move = investigated_move
        if player == provided.PLAYERX:
            return (highest_score, best_move)
        if player == provided.PLAYERO:
            return (lowest_score, best_move)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
