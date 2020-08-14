"""
Test suites for the game
"""

import poc_simpletest


def run_suite1(merge):
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
    suite.run_test(merge(line5), [5,12,7,0,0,0,1],"Test #5:")
    suite.run_test(merge(line6), [], "Test #6:")
    #report test results
    suite.report_results()
