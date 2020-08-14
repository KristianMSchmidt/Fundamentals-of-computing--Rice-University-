"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move

Done by Kristian Moeller Schmidt, october 2017

Inkluderer eksemplarisk test system
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.board=[0]

    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.board=list(configuration)

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self.board)

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.board[house_num]


    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for indx in self.board[1:]:
            if indx != 0:
                return False
        return True


    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """

        number_within_range = 0 < house_num < len(self.board)
        seeds_match = self.board[house_num] == house_num

        return number_within_range and seeds_match

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num) and house_num != 0:
            for house in range(house_num):
                self.board[house] +=1
            self.board[house_num]=0

        return self.board

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house_num in range(1,len(self.board)):
            if self.is_legal_move(house_num):
                return house_num
        return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
        After each move, move the seeds in the house closest to the store
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """

        copy=SolitaireMancala()
        copy.set_board(self.board)

        moves=[]
        while copy.choose_move()>0:
            moves.append(copy.choose_move())
            copy.apply_move(copy.choose_move())

        return moves

#Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())


# import test suite and run
#import poc_mancala_testsuite_v2 as poc_mancala_testsuite
#poc_mancala_testsuite.run_suite(SolitaireMancala)



"""
Test suites for the game"
"""

import poc_simpletest



def test_suite2():

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    #create boards to test
    b0=SolitaireMancala()

    b1=SolitaireMancala()
    config1=[0,1,2,3,4,5,7]
    b1.set_board(config1)

    b2=SolitaireMancala()
    config2=[0,0,0,0,0,0,1]
    b2.set_board(config2)

    b3=SolitaireMancala()
    config2=[5,0,0,0,0,0,0]
    b3.set_board(config2)

    # test the method
    suite.run_test(b0.is_game_won(), True, "Test #1:")
    suite.run_test(b1.is_game_won(), False, "Test #2:")
    suite.run_test(b2.is_game_won(), False, "Test #3:")
    suite.run_test(b3.is_game_won(), True, "Test #4:")

    #report test results
    suite.report_results()
test_suite2()

def test_suite3():

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    #create boards to test
    b0=SolitaireMancala()

    b1=SolitaireMancala()
    config1=[0,1,2,3,4,5,7]
    b1.set_board(config1)

    b2=SolitaireMancala()
    config2=[0,0,0,0,0,0,1]
    b2.set_board(config2)

    b3=SolitaireMancala()
    config2=[5,0,0,0,0,0,0]
    b3.set_board(config2)

    # test the method
    suite.run_test(b1.apply_move(1),  [1,0,2,3,4,5,7], "Test #1:")
    suite.run_test(b1.apply_move(5), [2,1,3,4,5,0,7], "Test #2:")
    suite.run_test(b1.apply_move(5), [2,1,3,4,5,0,7], "Test #3:")
    suite.run_test(b2.apply_move(6), [0,0,0,0,0,0,1], "Test #4:")

    #report results
    suite.report_results()
test_suite3()
