import unittest
import Fifteen_Puzzle3_recursive as fp


class TestFifteen_Puzzle(unittest.TestCase):


    def setUp(self):
        """
        Do the following before each test
        """
        pass
    
    def tearDown(self):
        """
        Do the following after each test
        """
        pass

    def test_solve_puzzle(self):
        puzzle =       fp.Puzzle(4,4, [[5,1,4,2],
                                   [12,8,9,3],
                                   [13,6,0,7],
                                  [10,14,11,15]])

        clone = puzzle.clone()
        move_string = puzzle.solve_puzzle()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)

    def test_solve_puzzle(self):
        puzzle =       fp.Puzzle(4,4, [[5,1,4,2],
                                   [12,8,3,0],
                                   [13,6,9,7],
                                  [10,14,11,15]])

        clone = puzzle.clone()
        move_string = puzzle.solve_puzzle()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)


    def test_solve_puzzle(self):
        puzzle =       fp.Puzzle(4,4, [[5,1,4,2],
                                      [12,8,3,0],
                                      [13,6,9,7],
                                      [10,14,11,15]])
        puzzle.update_puzzle("dllulu")
        print puzzle
        clone = puzzle.clone()
        move_string = puzzle.solve_puzzle()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)
        print puzzle


    def test_solve_puzzle(self):
        puzzle =       fp.Puzzle(4,4, [[5,1,4,2],
                                      [12,8,3,0],
                                      [13,6,9,7],
                                      [10,14,11,15]])
        puzzle.update_puzzle("dlluluddrrr")
        print puzzle
        clone = puzzle.clone()
        move_string = puzzle.solve_puzzle()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)
        print puzzle


    def test_solve_puzzle(self):
        puzzle =       fp.Puzzle(4,4, [[5,1,4,2],
                                      [12,8,3,0],
                                      [13,6,9,7],
                                      [10,14,11,15]])
        puzzle.update_puzzle("dlluluddrrrulul")

        clone = puzzle.clone()
        move_string = puzzle.solve_puzzle()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)

    def test_solve_2x2(self):

        puzzle =      fp.Puzzle(4,4, [[1,5,2,3],
                                      [4,0,6,7],
                                     [8,9,10,11],
                                     [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(1))
        clone = puzzle.clone()
        move_string = puzzle.solve_2x2()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)


    def test_solve_2x2(self):

        puzzle =      fp.Puzzle(4,4, [[5,4,2,3],
                                      [1,0,6,7],
                                     [8,9,10,11],
                                     [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(1))
        clone = puzzle.clone()
        move_string = puzzle.solve_2x2()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)



    def test_solve_2x2(self):

        puzzle =      fp.Puzzle(4,4, [[4,1,2,3],
                                      [5,0,6,7],
                                     [8,9,10,11],
                                     [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(1))
        clone = puzzle.clone()
        move_string = puzzle.solve_2x2()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)



    def test_solve_2x2(self):

        puzzle =      fp.Puzzle(2,2, [[1,3],[2,0]])

        self.assertTrue(puzzle.row1_invariant(1))
        clone = puzzle.clone()
        move_string = puzzle.solve_2x2()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)


    def test_solve_2x2(self):

        puzzle =      fp.Puzzle(2,2, [[3,2],[1,0]])

        self.assertTrue(puzzle.row1_invariant(1))
        clone = puzzle.clone()
        move_string = puzzle.solve_2x2()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)


    def test_solve_2x2(self):

        puzzle =      fp.Puzzle(2,2, [[2,1],[3,0]])

        self.assertTrue(puzzle.row1_invariant(1))
        clone = puzzle.clone()
        move_string = puzzle.solve_2x2()
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(0))
        self.assertEqual(puzzle._grid, clone._grid)


    def test_solve_row0_tile(self):

        puzzle =   fp.Puzzle(4,4, [[5,2,1,0],
                                   [6,4,3,7],
                                  [8,9,10,11],
                                  [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle =   fp.Puzzle(4,4, [[5,2,1,0],
                                   [6,3,4,7],
                                  [8,9,10,11],
                                  [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle =   fp.Puzzle(4,4, [[5,2,1,0],
                                   [3,6,4,7],
                                  [8,9,10,11],
                                  [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle =   fp.Puzzle(4,4, [[3,2,5,0],
                                   [1,6,4,7],
                                  [8,9,10,11],
                                  [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle =   fp.Puzzle(4,4, [[2,3,5,0],
                                   [1,6,4,7],
                                  [8,9,10,11],
                                  [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle =   fp.Puzzle(4,4, [[2,5,3,0],
                                   [1,6,4,7],
                                  [8,9,10,11],
                                  [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle =   fp.Puzzle(4,4, [[2,4,0,3],
                                   [1,5,6,7],
                                  [8,9,10,11],
                                  [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(1))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle =   fp.Puzzle(4,4, [[1,4,0,3],
                                   [2,5,6,7],
                                  [8,9,10,11],
                                  [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(1))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle =   fp.Puzzle(4,4, [[1,4,0,3],
                                   [5,2,6,7],
                                  [8,9,10,11],
                                  [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(1))
        self.assertEqual(puzzle._grid, clone._grid)




        #special case
        puzzle = fp.Puzzle(4,4, [[1,2,0,3],
                                [5,4,6,7],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(1))
        self.assertEqual(puzzle._grid, clone._grid)

        #special case
        puzzle = fp.Puzzle(4,4, [[1,2,3,0],
                                [5,4,6,7],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row0_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row1_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


    def test_solve_row1_tile(self):

        puzzle = fp.Puzzle(4,4, [[6,2,1,3],
                                [5,4,0,7],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(4,4, [[2,6,1,3],
                                [5,4,0,7],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle = fp.Puzzle(4,4, [[2,1,6,3],
                                [5,4,0,7],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.row0_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle = fp.Puzzle(4,4, [[2,1,5,3],
                                [6,4,0,7],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(2)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle = fp.Puzzle(4,4, [[2,1,5,3],
                                [4,6,0,7],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(2)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle = fp.Puzzle(4,4, [[7,1,5,3],
                                [4,6,2,0],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(3)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(3))
        self.assertEqual(puzzle._grid, clone._grid)



        puzzle = fp.Puzzle(4,4, [[5,1,7,3],
                                [4,6,2,0],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(3)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(3))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(4,4, [[5,1,3,7],
                                [4,6,2,0],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(3)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(3))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(4,4, [[5,1,3,4],
                                [7,6,2,0],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(3)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(3))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle = fp.Puzzle(4,4, [[5,1,3,4],
                                [2,6,7,0],
                                [8,9,10,11],
                                [12,13,14,15]])

        self.assertTrue(puzzle.row1_invariant(3))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(3)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(3))
        self.assertEqual(puzzle._grid, clone._grid)



        puzzle = fp.Puzzle(3,3, [[5,1,2],
                                [3,4,0],
                                [6,7,8]])

        self.assertTrue(puzzle.row1_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(2)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(3,3, [[1,5,2],
                                [3,4,0],
                                [6,7,8]])

        self.assertTrue(puzzle.row1_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(2)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle = fp.Puzzle(3,3, [[1,2,5],
                                [3,4,0],
                                [6,7,8]])

        self.assertTrue(puzzle.row1_invariant(2))
        clone = puzzle.clone()
        move_string = puzzle.solve_row1_tile(2)
        clone.update_puzzle(move_string)

        self.assertTrue(puzzle.row0_invariant(2))
        self.assertEqual(puzzle._grid, clone._grid)






    def test_row1_invariant(self):
        self.assertFalse(fp.Puzzle(4,4, [[4,2,1,3],[5,0,6,7],[8,9,10,11],[12,13,14,15]]).row1_invariant(1))
        self.assertTrue(fp.Puzzle(4,4, [[4,1,2,3],[5,0,6,7],[8,9,10,11],[12,13,14,15]]).row1_invariant(1))

        self.assertFalse(fp.Puzzle(4,4, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]).row1_invariant(2))
        self.assertFalse(fp.Puzzle(4,4, [[0,1,3,2],[4,5,0,7],[8,9,10,11],[12,13,14,15]]).row1_invariant(2))
        self.assertFalse(fp.Puzzle(4,4, [[6,1,7,3],[4,5,0,2],[8,9,10,11],[12,13,14,15]]).row1_invariant(2))
        self.assertFalse(fp.Puzzle(4,4, [[6,1,2,3],[4,5,0,7],[8,9,10,11],[12,14,13,15]]).row1_invariant(2))
        self.assertFalse(fp.Puzzle(4,4, [[6,1,2,3],[4,5,0,7],[9,8,10,11],[12,13,14,15]]).row1_invariant(2))
        self.assertFalse(fp.Puzzle(4,4, [[3,2,1,6],[5,4,0,7],[8,9,10,11],[12,13,14,15]]).row1_invariant(2))
        self.assertTrue(fp.Puzzle(4,4, [[6,2,1,3],[5,4,0,7],[8,9,10,11],[12,13,14,15]]).row1_invariant(2))

        self.assertFalse(fp.Puzzle(3,3, [[0,1,2],[3,4,5],[6,7,8]]).row1_invariant(1))
        self.assertTrue(fp.Puzzle(3,3, [[4,1,2],[3,0,5],[6,7,8]]).row1_invariant(1))
        self.assertFalse(fp.Puzzle(3,3, [[4,1,2],[5,0,3],[6,7,8]]).row1_invariant(1))
        self.assertFalse(fp.Puzzle(3,3, [[4,1,2],[3,0,5],[7,6,8]]).row1_invariant(1))

        self.assertTrue(fp.Puzzle(3,3, [[5,1,2],[3,4,0],[6,7,8]]).row1_invariant(2))
        self.assertFalse(fp.Puzzle(3,3, [[5,1,2],[3,4,0],[6,8,7]]).row1_invariant(2))


    def test_row0_invariant(self):
        self.assertTrue(fp.Puzzle(3,3, [[1,2,0],[3,4,5],[6,7,8]]).row0_invariant(2))
        self.assertFalse(fp.Puzzle(3,3, [[1,2,0],[3,4,5],[7,6,8]]).row0_invariant(2))
        self.assertFalse(fp.Puzzle(3,3, [[1,2,0],[4,3,5],[7,6,8]]).row0_invariant(2))
        self.assertFalse(fp.Puzzle(3,3, [[1,2,0],[5,4,3],[7,6,8]]).row0_invariant(2))
        self.assertFalse(fp.Puzzle(3,3, [[1,0,2],[3,4,5],[6,7,8]]).row0_invariant(2))

        self.assertTrue(fp.Puzzle(3,3, [[1,0,2],[3,4,5],[6,7,8]]).row0_invariant(1))
        self.assertFalse(fp.Puzzle(3,3, [[1,0,3],[2,4,5],[7,6,8]]).row0_invariant(2))

        self.assertFalse(fp.Puzzle(4,4, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]).row0_invariant(2))
        self.assertTrue(fp.Puzzle(4,4, [[2,1,0,3],[5,4,6,7],[8,9,10,11],[12,13,14,15]]).row0_invariant(2))
        self.assertFalse(fp.Puzzle(4,4, [[3,1,0,2],[5,4,6,7],[8,9,10,11],[12,13,14,15]]).row0_invariant(2))
        self.assertFalse(fp.Puzzle(4,4, [[2,1,0,3],[5,6,4,7],[8,9,10,11],[12,13,14,15]]).row0_invariant(2))
        self.assertFalse(fp.Puzzle(4,4, [[2,1,0,3],[5,4,6,7],[9,8,10,11],[12,13,14,15]]).row0_invariant(2))


    def test_solve_col0_tile(self):

        # all 3x3 cases
        puzzle = fp.Puzzle(3,3, [[3,1,2],
                                [6,4,5],
                                 [0,7,8]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,2))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle = fp.Puzzle(3,3, [[6,1,2],
                                [3,4,5],
                                 [0,7,8]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,2))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(3,3, [[4,1,2],
                                [3,6,5],
                                 [0,7,8]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,2))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(3,3, [[4,1,2],
                                [3,5,6],
                                 [0,7,8]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,2))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(3,3, [[4,1,6],
                                [3,5,2],
                                 [0,7,8]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,2))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(3,3, [[4,6,1],
                                [3,5,2],
                                 [0,7,8]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,2))
        self.assertEqual(puzzle._grid, clone._grid)

        # 4x4 cases

        puzzle = fp.Puzzle(4,4, [[8,1,2,3],
                                [4,5,6,7],
                                 [12,9,10,11],
                                 [0,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(3,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,3))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle = fp.Puzzle(4,4, [[8,1,2,3],
                                [12,5,6,7],
                                 [4,9,10,11],
                                 [0,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(3,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,3))
        self.assertEqual(puzzle._grid, clone._grid)
        #####################
        puzzle = fp.Puzzle(4,4, [[12,1,2,3],
                                [8,5,6,7],
                                 [4,9,10,11],
                                 [0,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(3,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,3))
        self.assertEqual(puzzle._grid, clone._grid)

        #####################
        puzzle = fp.Puzzle(4,4, [[11,1,2,3],
                                [8,5,6,7],
                                 [4,9,10,12],
                                 [0,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(3,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,3))
        self.assertEqual(puzzle._grid, clone._grid)

        #####################
        puzzle = fp.Puzzle(4,4, [[11,1,2,3],
                                [8,5,12,7],
                                 [4,9,10,6],
                                 [0,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(3,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,3))
        self.assertEqual(puzzle._grid, clone._grid)

        #####################
        puzzle = fp.Puzzle(4,4, [[11,1,12,3],
                                [8,5,2,7],
                                 [4,9,10,6],
                                 [0,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(3,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,3))
        self.assertEqual(puzzle._grid, clone._grid)

        #####################
        puzzle = fp.Puzzle(4,4, [[4,1,6,3],
                                [8,5,2,7],
                                 [0,9,10,11],
                                 [12,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,3))
        self.assertEqual(puzzle._grid, clone._grid)


        #####################
        puzzle = fp.Puzzle(4,4, [[8,1,6,3],
                                [4,5,2,7],
                                 [0,9,10,11],
                                 [12,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,3))
        self.assertEqual(puzzle._grid, clone._grid)

        #####################
        puzzle = fp.Puzzle(4,4, [[7,1,6,3],
                                [4,5,2,8],
                                 [0,9,10,11],
                                 [12,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,3))
        self.assertEqual(puzzle._grid, clone._grid)

        #####################
        puzzle = fp.Puzzle(4,4, [[7,1,6,3],
                                [4,8,2,5],
                                 [0,9,10,11],
                                 [12,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,3))
        self.assertEqual(puzzle._grid, clone._grid)

        #####################
        puzzle = fp.Puzzle(4,4, [[7,1,6,8],
                                [4,3,2,5],
                                 [0,9,10,11],
                                 [12,13,14,15]])

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,3))
        self.assertEqual(puzzle._grid, clone._grid)

        #####################
        matrix = [[col + row*3  for col in range(3)] for row in range(10)]
        matrix[9][0]=0
        matrix[0][2]=27
        matrix[0][0]=2

        puzzle = fp.Puzzle(10,3, matrix)
        self.assertTrue(puzzle.lower_row_invariant(9,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(9)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(8,2))
        self.assertEqual(puzzle._grid, clone._grid)

        #####################
        matrix = [[col + row*10  for col in range(10)] for row in range(3)]
        matrix[2][0]=0
        matrix[1][8]=20
        matrix[0][0]=18

        puzzle = fp.Puzzle(3,10, matrix)

        self.assertTrue(puzzle.lower_row_invariant(2,0))
        clone = puzzle.clone()
        move_string = puzzle.solve_col0_tile(2)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(1,9))
        self.assertEqual(puzzle._grid, clone._grid)



    def test_solve_interior_tile_case2(self):
        puzzle = fp.Puzzle(4,4, [[1,10,3,9],
                                [4,5,6,7],
                                [8,11,2,0],
                                [12,13,14,15]])
        self.assertTrue(puzzle.lower_row_invariant(2,3))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(2,3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,2))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(4,4, [[1,2,3,9],
                                [4,5,6,7],
                                [8,0,10,11],
                                [12,13,14,15]])
        self.assertTrue(puzzle.lower_row_invariant(2,1))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(2,1)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,0))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(4,4, [[15,2,3,9],
                                [4,5,6,7],
                                [8,1,10,11],
                                [12,13,14,0]])
        self.assertTrue(puzzle.lower_row_invariant(3,3))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(3,3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(3,2))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(4,4, [[1,2,3,9],
                                [4,5,13,7],
                                [8,6,10,11],
                                [12,0,14,15]])
        self.assertTrue(puzzle.lower_row_invariant(3,1))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(3,1)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(3,0))
        self.assertEqual(puzzle._grid, clone._grid)


        puzzle = fp.Puzzle(4,4, [[8,2,3,9],
                                [4,5,6,7],
                                [11,1,10,0],
                                [12,13,14,15]])
        self.assertTrue(puzzle.lower_row_invariant(2,3))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(2,3)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,2))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(3,3, [[1,6,2],
                                 [3,4,5],
                                 [7,0,8]])
        self.assertTrue(puzzle.lower_row_invariant(2,1))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(2,1)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,0))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(3,3, [[1,6,7],
                                 [3,4,5],
                                 [6,0,8]])
        self.assertTrue(puzzle.lower_row_invariant(2,1))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(2,1)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,0))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(3,3, [[1,6,3],
                                 [7,4,5],
                                 [6,0,8]])
        self.assertTrue(puzzle.lower_row_invariant(2,1))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(2,1)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,0))
        self.assertEqual(puzzle._grid, clone._grid)


    def test_solve_interior_tile_case1(self):

        puzzle = fp.Puzzle(4,4, [[1,9,2,3], [4,5,6,7],[8,0,10,11], [12,13,14,15]])
        self.assertTrue(puzzle.lower_row_invariant(2,1))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(2,1)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(2,0))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(4,4, [[1,13,2,3], [4,5,6,7],[8,9,10,11], [12,0,14,15]])
        self.assertTrue(puzzle.lower_row_invariant(3,1))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(3,1)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(3,0))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(4,4, [[1,5,2,3], [4,13,6,7],[8,9,10,11], [12,0,14,15]])
        self.assertTrue(puzzle.lower_row_invariant(3,1))
        clone = puzzle.clone()
        move_string = puzzle.solve_interior_tile(3,1)
        clone.update_puzzle(move_string)
        self.assertTrue(puzzle.lower_row_invariant(3,0))
        self.assertEqual(puzzle._grid, clone._grid)

        puzzle = fp.Puzzle(4,4, [[1,5,2,3], [4,9,6,7],[8,13,9,11], [12,0,14,15]])
        self.assertTrue(puzzle.lower_row_invariant(3,1))
        puzzle.solve_interior_tile(3,1)
        self.assertTrue(puzzle.lower_row_invariant(3,0))

        puzzle = fp.Puzzle(4,4, [[1,5,2,3], [4,9,6,15],[8,13,9,7], [12,11,14,0]])
        self.assertTrue(puzzle.lower_row_invariant(3,3))
        puzzle.solve_interior_tile(3,3)
        self.assertTrue(puzzle.lower_row_invariant(3,2))

        puzzle = fp.Puzzle(4,3, [[1,7,3], [4,2,5], [6,0,8],[9,10,11]])
        self.assertTrue(puzzle.lower_row_invariant(2,1))
        puzzle.solve_interior_tile(2,1)
        self.assertTrue(puzzle.lower_row_invariant(2,0))

    def test_lower_row_invariant_condition_1(self):
        self.assertEqual(fp.Puzzle(1,1).lower_row_invariant(0,0), True)
        self.assertEqual(fp.Puzzle(1,2).lower_row_invariant(0,0), True)
        self.assertEqual(fp.Puzzle(1,2).lower_row_invariant(0,1), False)
        self.assertEqual(fp.Puzzle(2,1).lower_row_invariant(0,0), True)
        self.assertEqual(fp.Puzzle(2,1).lower_row_invariant(1,0), False)
        self.assertEqual(fp.Puzzle(2,2).lower_row_invariant(0,0), True)
        self.assertEqual(fp.Puzzle(2,2).lower_row_invariant(0,1), False)
        self.assertEqual(fp.Puzzle(2,2).lower_row_invariant(1,0), False)
        self.assertEqual(fp.Puzzle(3,2).lower_row_invariant(1,1), False)
        self.assertEqual(fp.Puzzle(4,4).lower_row_invariant(0,0), True)
        self.assertEqual(fp.Puzzle(4,4).lower_row_invariant(1,1), False)
        self.assertEqual(fp.Puzzle(4,4).lower_row_invariant(2,3), False)
        self.assertEqual(fp.Puzzle(4,4).lower_row_invariant(3,1), False)

    def test_lower_row_invariant_condition_2(self):
        self.assertEqual(fp.Puzzle(2,2, [[1,0],[2,3]]).lower_row_invariant(0,1), True)
        self.assertEqual(fp.Puzzle(2,2, [[1,0],[3,2]]).lower_row_invariant(0,1), False)

        self.assertEqual(fp.Puzzle(2,3, [[0,1,2],[5,4,3]]).lower_row_invariant(0,0), False)

        self.assertEqual(fp.Puzzle(3,3, [[0,1,2],[3,4,5],[6,8,7]]).lower_row_invariant(0,0), False)
        self.assertEqual(fp.Puzzle(3,3, [[0,1,2],[4,5,3],[6,7,8]]).lower_row_invariant(0,0), False)

        self.assertEqual(fp.Puzzle(4,4, [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,15,14]]).lower_row_invariant(0,0), False)
        self.assertEqual(fp.Puzzle(4,4, [[0,1,2,3],[4,5,6,7],[8,10,9,11],[12,13,14,15]]).lower_row_invariant(0,0), False)
        self.assertEqual(fp.Puzzle(4,4, [[0,1,2,3],[7,5,6,4],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(0,0), False)
        self.assertEqual(fp.Puzzle(4,4, [[5,1,2,3],[4,0,6,7],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(1,1), True)
        self.assertEqual(fp.Puzzle(4,4, [[5,1,2,3],[4,7,6,0],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(1,3), True)
        self.assertEqual(fp.Puzzle(4,4, [[5,1,2,3],[4,77,6,7],[0,9,10,11],[12,13,14,15]]).lower_row_invariant(2,0), True)
        self.assertEqual(fp.Puzzle(4,4, [[5,1,2,3],[4,77,6,0],[0,9,10,11],[13,12,14,15]]).lower_row_invariant(2,0), False)

    def test_lower_row_invariant_condition_3(self):
        self.assertEqual(fp.Puzzle(2,2, [[1,2],[0,3]]).lower_row_invariant(1,0), True)
        self.assertEqual(fp.Puzzle(2,2, [[1,2],[3,0]]).lower_row_invariant(1,1), True)
        self.assertEqual(fp.Puzzle(2,2, [[1,0],[2,3]]).lower_row_invariant(0,1), True)

        self.assertEqual(fp.Puzzle(3,3, [[1,2,0],[3,4,5],[6,7,8]]).lower_row_invariant(0,2), True)
        self.assertEqual(fp.Puzzle(3,3, [[1,0,2],[3,4,5],[6,7,8]]).lower_row_invariant(0,1), True)
        self.assertEqual(fp.Puzzle(3,3, [[2,0,1],[3,4,5],[6,7,8]]).lower_row_invariant(0,1), False)

        self.assertEqual(fp.Puzzle(3,3, [[1,2,3],[0,4,5],[6,7,8]]).lower_row_invariant(1,0), True)
        self.assertEqual(fp.Puzzle(3,3, [[1,2,3],
                                        [0,5,4],
                                        [6,7,8]]).lower_row_invariant(1,0), False)
        self.assertEqual(fp.Puzzle(3,3, [[1,2,3],[4,5,0],[6,7,8]]).lower_row_invariant(1,2), True)
        self.assertEqual(fp.Puzzle(3,3, [[3,4,5],[1,0,2],[6,7,8]]).lower_row_invariant(1,1), False)

        self.assertEqual(fp.Puzzle(4,4, [[6,1,2,3],[4,5,0,7],[8,9,10,11],[12,13,14,15]]).lower_row_invariant(1,2), True)
        self.assertEqual(fp.Puzzle(4,4, [[6,1,2,3],[4,5,0,7],[9,8,10,11],[12,13,14,15]]).lower_row_invariant(1,2), False)

        self.assertEqual(fp.Puzzle(4,4, [[10,1,2,3],[4,5,6,7],[8,9,0,11],[12,13,14,15]]).lower_row_invariant(2,2), True)
        self.assertEqual(fp.Puzzle(4,4, [[10,1,2,3],[4,5,6,7],[8,9,0,11],[15,13,14,12]]).lower_row_invariant(2,2), False)

        self.assertEqual(fp.Puzzle(4,4, [[12,1,2,3],[4,5,6,7],[8,9,10,11],[0,14,13,15]]).lower_row_invariant(3,0), False)




if __name__ == '__main__':
    unittest.main()
