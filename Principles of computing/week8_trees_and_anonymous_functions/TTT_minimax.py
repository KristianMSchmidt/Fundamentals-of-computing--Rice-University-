
"""
Mini-max Tic-Tac-Toe Player

Kristian Moeller Schmidt.
Submitted version.
Works just fine.
But can be made more elegant.

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
    #if no legal moves, return (score of board, (-1,-1))
    if board.check_win() != None:
        final_result = board.check_win()
        score_of_final_board = SCORES[final_result]
        no_possible_moves_left = (-1,-1)
        return (score_of_final_board, no_possible_moves_left)

    else:
        #list of all legal moves
        legal_moves = board.get_empty_squares()
        board_clones = []
        for indx in range(0, len(legal_moves)):
            move = legal_moves[indx]
            clone = board.clone()
            clone.move(move[0], move[1], player)
            board_clones.append(clone)

        if player == provided.PLAYERX:
            best_score = - 1
            best_move = None
            for indx in range(0, len(board_clones)):
                investigated_move = legal_moves[indx]
                clone = board_clones[indx]
                score = mm_move(clone, provided.PLAYERO)[0]
                if score == 1:
                    return (score, investigated_move)
                elif score >= best_score:
                    best_score = score
                    best_move = investigated_move
            return (best_score, best_move)


        if player == provided.PLAYERO:
            best_score = 1
            best_move = None
            for indx in range(0, len(board_clones)):
                clone = board_clones[indx]
                score = mm_move(clone, provided.PLAYERX)[0]
                if score == -1:
                    best_move = legal_moves[indx]
                    return (score, best_move)
                elif score <= best_score:
                    best_move = legal_moves[indx]
                    best_score = score
            return (best_score, best_move)


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
