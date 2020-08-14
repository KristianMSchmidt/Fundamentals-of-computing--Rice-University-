import unittest


import TTT_minimax_version2 as ttt
from TTT_minimax_version2 import *

#import TTT_minimax as ttt
#from TTT_minimax import *

class TestTTT_minimax(unittest.TestCase):


    def setUp(self):
        """
        Do the following after each test
        """

        #board won by player X
        self.board_won_by_X = provided.TTTBoard(3,False,[[provided.PLAYERX,provided.PLAYERX,provided.PLAYERX],
                                                     [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                                     [provided.PLAYERO, provided.PLAYERO, provided.PLAYERX]])

        self.board_won_by_O = provided.TTTBoard(3,False,[[provided.PLAYERX,provided.PLAYERX,provided.PLAYERO],
                                                     [provided.PLAYERO, provided.PLAYERO, provided.PLAYERX],
                                                     [provided.PLAYERO, provided.PLAYERO, provided.PLAYERX]])
        self.board_draw = provided.TTTBoard(3,False,[[provided.PLAYERX,provided.PLAYERX,provided.PLAYERO],
                                                     [provided.PLAYERO, provided.PLAYERO, provided.PLAYERX],
                                                     [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])

        self.board_both_choose_20 = provided.TTTBoard(3,False,[[provided.PLAYERO,provided.PLAYERX,provided.PLAYERX],
                                                 [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                                 [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]])

        self.board5 = provided.TTTBoard(3,False,[[provided.PLAYERO,provided.PLAYERX,provided.PLAYERO],
                                                 [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                                 [provided.EMPTY, provided.EMPTY, provided.PLAYERX]])

        self.board6 = provided.TTTBoard(3,False,[[provided.PLAYERO,provided.PLAYERX,provided.EMPTY],
                                                [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                                [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]])

        self.b11 = provided.TTTBoard(3,False,[[provided.PLAYERO,provided.PLAYERX,provided.PLAYERX],
                                            [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                         [provided.PLAYERO, provided.PLAYERO, provided.PLAYERX]])


        self.b12 = provided.TTTBoard(3,False,[[provided.PLAYERO,provided.PLAYERX,provided.PLAYERX],
                                            [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                            [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]])


        self.b121 = provided.TTTBoard(3,False,[[provided.PLAYERO,provided.PLAYERX,provided.PLAYERX],
                                               [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                               [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])

        self.b =  provided.TTTBoard(3,False,[[provided.PLAYERO,provided.PLAYERX,provided.EMPTY],
                                               [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                               [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]])


        self.b3 =  provided.TTTBoard(3,False,[[provided.PLAYERO,provided.PLAYERX,provided.EMPTY],
                                               [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                               [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])


        self.b_empty = provided.TTTBoard(3,False,[[1,1,1],
                                                  [1,1,1],
                                                  [1,1,1]])

        self.b_almost_empty = provided.TTTBoard(3,False,[[1,1,2],
                                                  [1,1,1],
                                                  [1,1,1]])


        self.board_44 = provided.TTTBoard(4,False,[[3,3,3,1],
                                                   [3,2,2,2],
                                                   [2,1,3,2],
                                                   [3,3,2,3]])


    def tearDown(self):
        """
        Do the following after each test
        """
        pass

    def test_mm_move(self):
        self.assertEqual(mm_move(self.board_won_by_X, provided.PLAYERX), (1, (-1, -1)))
        self.assertEqual(mm_move(self.board_won_by_X, provided.PLAYERO), (1, (-1, -1)))

        self.assertEqual(mm_move(self.board_won_by_O, provided.PLAYERX), (-1, (-1, -1)))
        self.assertEqual(mm_move(self.board_won_by_O, provided.PLAYERO), (-1, (-1, -1)))

        self.assertEqual(mm_move(self.board_draw, provided.PLAYERX), (0, (-1, -1)))
        self.assertEqual(mm_move(self.board_draw, provided.PLAYERO), (0, (-1, -1)))

        self.assertEqual(mm_move(self.board_both_choose_20, provided.PLAYERX), (1, (2,0) ))
        self.assertEqual(mm_move(self.board_both_choose_20, provided.PLAYERO), (-1, (2,0) ))

        self.assertEqual(mm_move(self.board5, provided.PLAYERX), (1, (2,1) ))
        self.assertEqual(mm_move(self.board5, provided.PLAYERO), (-1, (2,0) ))

        self.assertEqual(mm_move(self.board6, provided.PLAYERO), (-1, (2,0) ))
        self.assertEqual(mm_move(self.board6, provided.PLAYERX), (0, (2,0) ))

        self.assertEqual(mm_move(self.b12, provided.PLAYERX), (1, (2,0) ))
        self.assertEqual(mm_move(self.b121, provided.PLAYERO), (1, (-1,-1) ))

        self.assertEqual(mm_move(self.b, provided.PLAYERX), (0, (2,0) ))
        self.assertEqual(mm_move(self.b, provided.PLAYERO), (-1, (2,0) ))

        self.assertEqual(mm_move(self.b3, provided.PLAYERO), (0, (0,2) ))

        self.assertEqual(mm_move(self.board_44, 3), (-1, (0,3) ))
        self.assertEqual(mm_move(self.board_44, 2), (0, (0,3) ))

        self.b_draw1 = provided.TTTBoard(3,False,[[2,3,2],
                                                   [3,3,2],
                                                   [2,2,3]])

        self.assertEqual(mm_move(self.b_draw1, provided.PLAYERO)[0], 0)
        self.assertEqual(mm_move(self.b_draw1, provided.PLAYERX)[0], 0)

        self.b_draw1 = provided.TTTBoard(3,False,[[2,3,2],
                                                   [3,1,2],
                                                   [2,1,3]])

        self.assertEqual(mm_move(self.b_draw1, provided.PLAYERO)[0], 0)
        self.assertEqual(mm_move(self.b_draw1, provided.PLAYERX)[0], 1)

        self.b_draw1 = provided.TTTBoard(3,False,[[1,1,3],
                                                   [2,1,3],
                                                   [3,1,2]])
        self.assertEqual(mm_move(self.b_draw1, provided.PLAYERX), (0, (1,1)))

        self.b_draw1 = provided.TTTBoard(3,False,[[1,1,2],
                                                   [3,1,2],
                                                   [2,1,3]])
        self.assertEqual(mm_move(self.b_draw1, provided.PLAYERO), (0, (1,1)))

        self.assertEqual(mm_move(self.b_empty, provided.PLAYERX)[0], 0)

        self.assertEqual(mm_move(self.b_almost_empty, provided.PLAYERO)[0], 0)

if __name__ == '__main__':
    unittest.main()
