"""
Merge function for 2048 game. Virker 100%
By Kristian
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    non_zeros=[]
    zeros=[]
    tiles=[]
    actual_is_tiled=False

    for number in line:
        if number != 0:
            non_zeros.append(number)
        else:
            zeros.append(0)

    for index in range(len(non_zeros)):
        actual=non_zeros[index]

        if actual_is_tiled:
            zeros.append(0)
            actual_is_tiled=False
        elif index<len(non_zeros)-1:
            next_num=non_zeros[index+1]
            if actual != next_num:
                tiles.append(actual)
            else:
                tiles.append(actual+next_num)
                actual_is_tiled=True
        else:
            tiles.append(actual)

    return tiles+zeros


"""
Test suites for the game
"""

import poc_simpletest

def test_suite1():
    """
    Test merge function
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    #create data to test
    line1=[2, 0, 2, 4]
    line2=[0, 0, 2, 2]
    line3=[2, 2, 0, 0]
    line4=[2, 2, 2, 2, 2]
    line5=[0,5,0,6,6,0,7]
    line6=[]
    # test get_num_seeds
    suite.run_test(merge(line1), [4,4,0,0], "Test #1:")
    suite.run_test(merge(line2), [4,0,0,0], "Test #2:")
    suite.run_test(merge(line3), [4,0,0,0], "Test #3:")
    suite.run_test(merge(line4), [4,4,2,0,0], "Test #4:")
    suite.run_test(merge(line5), [5,12,7,0,0,0,0],"Test #5:")
    suite.run_test(merge(line6), [], "Test #6:")
    #report test results
    suite.report_results()
test_suite1()
