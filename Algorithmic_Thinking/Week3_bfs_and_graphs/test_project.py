import unittest

import project as p

class Testproject(unittest.TestCase):


    def setUp(self):
        """
        Do the following after each test
        """
        pass

    def tearDown(self):
        """
        Do the following after each test
        """
        pass

    def test_cc_visited(self):
        """
        Takes the undirected graph ugraph and returns a list of sets, where each set consists of all the nodes
        (and nothing else) in a connected component, and there is exactly one set in the list for each connected
        component in ugraph and nothing else.
        """
        graph1 = {0: set()}
        self.assertEqual(p.cc_visited(graph1), [set([0])])

        graph2 = {0: set([1]), 1: set([0])}
        self.assertEqual(p.cc_visited(graph2), [set([0,1])])

        graph3 = {0: set([]), 1: set([])}
        self.assertItemsEqual(p.cc_visited(graph3), [set([0]), set([1])])

        graph4 = {0: set([]), 1: set([2]), 2: set([1])}
        self.assertItemsEqual(p.cc_visited(graph4), [set([0]), set([1,2])])

        graph6 = {"a": set([]), "b": set(["c"]), "c": set(["d","b"]), "d":set(["e", "c"]), "e":set(["d"]) }
        self.assertItemsEqual(p.cc_visited(graph6), [set(["a"]), set(["b","c", "d", "e"])])



    def test_bfs_visited(self):
        """
        Takes the undirected graph ugraph and the node start_node and returns the set consisting of all nodes that are visited
        by a breadth-first search that starts at start_node. (i.e. returns the connected component of the start node)
        """

        graph1 = {0: set()}
        self.assertEqual(p.bfs_visited(graph1, 0), set([0]))

        graph2 = {0: set([1]), 1: set([0])}
        self.assertEqual(p.bfs_visited(graph2,0 ), set([0,1]))
        self.assertEqual(p.bfs_visited(graph2,1 ), set([0,1]))

        graph3 = {0: set([]), 1: set([])}
        self.assertEqual(p.bfs_visited(graph3,0 ), set([0]))
        self.assertEqual(p.bfs_visited(graph3,1 ), set([1]))

        graph4 = {0: set([]), 1: set([])}
        self.assertEqual(p.bfs_visited(graph4,0 ), set([0]))
        self.assertEqual(p.bfs_visited(graph4,1 ), set([1]))

        graph5 = {0: set([]), 1: set([2]), 2: set([1])}
        self.assertEqual(p.bfs_visited(graph5,0 ), set([0]))
        self.assertEqual(p.bfs_visited(graph5,2 ), set([1,2]))

        graph6 = {"a": set([]), "b": set(["c"]), "c": set(["d","b"]), "d":set(["e", "c"]), "e":set(["d"]) }
        self.assertEqual(p.bfs_visited(graph6,"e" ), set(["b","c", "d", "e"]))
        self.assertEqual(p.bfs_visited(graph6,"a" ), set(["a"]))


if __name__ == '__main__':
    unittest.main()
