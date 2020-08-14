import unittest

#import project as p
import alg_project3_solution as p

class Test_project(unittest.TestCase):

    def setUp(self):
        """
        Do the following after each test
        """
        # self.apoc_1 = Apocalypse(5,5, [(1,1)], [(2,2)], [(4,4)])


    def tearDown(self):
        """
        Do the following after each test
        """
        pass




    def test_hierarchical_clustering2(self):

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,  10,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1,   2,   10, 0.01)

        self.assertEqual(p.hierarchical_clustering([], 0), [])
        self.assertEqual(p.hierarchical_clustering([cluster0], 1), [cluster0])
        self.assertEqual(p.hierarchical_clustering([cluster0, cluster1], 2), [cluster0, cluster1])

    def test_hierarchical_clustering3(self):

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,  10, 0)
        cluster1 = p.c.Cluster(set(["DK"]), 1,   2,   2, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 60, 1, 0.05)

        clone0 = cluster0.copy()
        clone1 = cluster1.copy()
        clone2 = cluster2.copy()

        result = set((p.hierarchical_clustering([cluster0, cluster1, cluster2], 1))[0].fips_codes())
        expected = set(((clone0.merge_clusters(clone1)).merge_clusters(clone2)).fips_codes())

        self.assertEqual(result, expected)


    def test_hierarchical_clustering4(self):

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,  10,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1,   2,   10, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 60, 10, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 2,100000000, 3) #cluster1.merge_clusters(cluster2)

        clone0 = cluster0.copy()
        clone1 = cluster1.copy()
        clone2 = cluster2.copy()
        clone3 = cluster3.copy()


        result = p.hierarchical_clustering([cluster0, cluster1, cluster2, cluster3], 4)
        expected = [cluster0, cluster1, cluster2, cluster3]

        self.assertEqual(result, expected)


    def test_hierarchical_clustering5(self):

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,  10,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1,   2,   10, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 60, 10, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 2,100000000, 3) #cluster1.merge_clusters(cluster2)

        clone0 = cluster0.copy()
        clone1 = cluster1.copy()
        clone2 = cluster2.copy()
        clone3 = cluster3.copy()


        result = p.hierarchical_clustering([cluster0, cluster1, cluster2, cluster3], 3)
        result_str = ""
        for res in result:
            result_str += str(res)

        expected = [clone3, clone0.merge_clusters(clone1), clone2]
        exp_str = ""
        for exp in expected:
            exp_str += str(exp)

        #self.assertEqual(result_str, exp_str)


    def test_hierarchical_clustering6(self):

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,  10,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1,   2,   10, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 60, 10, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 2,100000000, 3) #cluster1.merge_clusters(cluster2)

        clone0 = cluster0.copy()
        clone1 = cluster1.copy()
        clone2 = cluster2.copy()
        clone3 = cluster3.copy()


        result = p.hierarchical_clustering([cluster0, cluster1, cluster2, cluster3], 2)
        result_str = ""
        for res in result:
            result_str += str(res)

        expected = [clone0.merge_clusters(clone1.merge_clusters(clone3)), clone2]
        exp_str = ""
        for exp in expected:
            exp_str += str(exp)

        self.assertEqual(result_str, exp_str)


    def test_hierarchical_clustering7(self):

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,  10,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1,   2,   10, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 60, 10, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 2,100000000, 3) #cluster1.merge_clusters(cluster2)

        clone0 = cluster0.copy()
        clone1 = cluster1.copy()
        clone2 = cluster2.copy()
        clone3 = cluster3.copy()


        result = p.hierarchical_clustering([cluster0, cluster1, cluster2, cluster3], 1)
        result_str = ""
        for res in result:
            result_str += str(res)

        expected = [(clone0.merge_clusters(clone1.merge_clusters(clone3))).merge_clusters(clone2)]
        exp_str = ""
        for exp in expected:
            exp_str += str(exp)

        self.assertEqual(result_str, exp_str)

    def test_closest_pair_functions(self):

        cluster1 = p.c.Cluster(set(["DK"]), 1, 2, 100, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 6, 200, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 2,100000000, 3) #cluster1.merge_clusters(cluster2)
        cluster4 = p.c.Cluster(set(["NL"]), 5, 6,4,4)
        cluster5 = p.c.Cluster(set(["NL"]), 5, 3, 100, 0.01)

        self.assertEqual(p.slow_closest_pair([]), (float("inf"), -1, -1))
        self.assertEqual(p.slow_closest_pair([]), p.fast_closest_pair([]))

        self.assertEqual(p.slow_closest_pair([cluster1]), (float("inf"), -1, -1))
        self.assertEqual(p.slow_closest_pair([cluster1]), p.fast_closest_pair([cluster1]))


        self.assertEqual(p.slow_closest_pair([cluster1, cluster1]), (0.0, 0, 1))
        self.assertEqual(p.slow_closest_pair([cluster1, cluster1]), p.fast_closest_pair([cluster1, cluster1]))

        self.assertEqual(p.slow_closest_pair([cluster1, cluster2, cluster3, cluster4]), (1, 1, 3))
        self.assertEqual(p.slow_closest_pair([cluster1, cluster2, cluster3, cluster4]), p.fast_closest_pair([cluster1, cluster2, cluster3, cluster4]))


        self.assertEqual(p.slow_closest_pair([cluster1, cluster2, cluster3]), (3, 0, 2))
        self.assertEqual(p.slow_closest_pair([cluster1, cluster2, cluster3]), p.fast_closest_pair([cluster1, cluster2, cluster3]))

        self.assertEqual(p.slow_closest_pair([cluster1, cluster2, cluster3, cluster4, cluster5]), (1, 1, 3))
        self.assertEqual(p.slow_closest_pair([cluster1, cluster2, cluster3, cluster4, cluster5]), p.fast_closest_pair([cluster1, cluster2, cluster3, cluster4, cluster5]))

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,0,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1, 2, 100, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 6, 200, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 2,100000000, 3) #cluster1.merge_clusters(cluster2)
        cluster4 = p.c.Cluster(set(["NL"]), 5, 6,4,4)
        cluster5 = p.c.Cluster(set(["NL"]), 5, 6.1, 100, 0.01)
        cluster6 = p.c.Cluster(set(["hl"]), 6,13, 0,0)
        cluster7 = p.c.Cluster(set(["hl"]), 6.5, 15, 0,0)
        cluster8 = p.c.Cluster(set(["hl"]), 8, 13, 0,0)
        cluster_list = [cluster0, cluster1, cluster2, cluster3, cluster4, cluster5, cluster6, cluster7, cluster8]

        self.assertEqual(p.slow_closest_pair(cluster_list), p.fast_closest_pair(cluster_list))

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,0,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1, 2, 100, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 6, 200, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 2,100000000, 3) #cluster1.merge_clusters(cluster2)
        cluster4 = p.c.Cluster(set(["NL"]), 5, 6,4,4)
        cluster5 = p.c.Cluster(set(["NL"]), 5, 6.1, 100, 0.01)
        cluster6 = p.c.Cluster(set(["hl"]), 6, 13, 0,0)
        cluster7 = p.c.Cluster(set(["hl"]), 6.5, 15, 0,0)
        cluster8 = p.c.Cluster(set(["hl"]), 8, 13, 0,0)
        cluster_list = [cluster0, cluster1, cluster2, cluster3, cluster4, cluster5, cluster6, cluster7, cluster8]
        #print p.slow_closest_pair(cluster_list)
        self.assertEqual(p.slow_closest_pair(cluster_list), p.fast_closest_pair(cluster_list))

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,0,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1, 2, 100, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 6, 200, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 2,100000000, 3) #cluster1.merge_clusters(cluster2)
        cluster4 = p.c.Cluster(set(["NL"]), 5, 50, 4,4)
        cluster5 = p.c.Cluster(set(["NL"]), 5, 100, 100, 0.01)
        cluster6 = p.c.Cluster(set(["hl"]), 6, 13, 0,0)
        cluster7 = p.c.Cluster(set(["hl"]), 6.5, 15, 0,0)
        cluster8 = p.c.Cluster(set(["hl"]), 8, 13, 0,0)
        cluster_list = [cluster0, cluster1, cluster2, cluster3, cluster4, cluster5, cluster6, cluster7, cluster8]
        #print p.slow_closest_pair(cluster_list)
        self.assertEqual(p.slow_closest_pair(cluster_list), p.fast_closest_pair(cluster_list))

        cluster0 = p.c.Cluster(set(["Al"]), 1.1, 10,0,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1, 2, 100, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 6, 200, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 30,100000000, 3) #cluster1.merge_clusters(cluster2)
        cluster4 = p.c.Cluster(set(["NL"]), 5, 50, 4,4)
        cluster5 = p.c.Cluster(set(["NL"]), 5, 100, 100, 0.01)
        cluster6 = p.c.Cluster(set(["hl"]), 6, 13, 0,0)
        cluster7 = p.c.Cluster(set(["hl"]), 30, 15, 0,0)
        cluster8 = p.c.Cluster(set(["hl"]), 40, 13, 0,0)
        cluster_list = [cluster0, cluster1, cluster2, cluster3, cluster4, cluster5, cluster6, cluster7, cluster8]
        #print p.slow_closest_pair(cluster_list)
        self.assertEqual(p.slow_closest_pair(cluster_list), p.fast_closest_pair(cluster_list))

        cluster0 = p.c.Cluster(set(["Al"]), 0, 10,0,0)
        cluster1 = p.c.Cluster(set(["DK"]), 1, 2, 100, 0.01)
        cluster2 = p.c.Cluster(set(["SW"]), 4, 20, 200, 0.05)
        cluster3 = p.c.Cluster(set(["Brasil"]), 4, 30,100000000, 3) #cluster1.merge_clusters(cluster2)
        cluster4 = p.c.Cluster(set(["NL"]), 5, 50, 4,4)
        cluster5 = p.c.Cluster(set(["NL"]), 5, 100, 100, 0.01)
        cluster6 = p.c.Cluster(set(["hl"]), 20, 13, 0,0)
        cluster7 = p.c.Cluster(set(["hl"]), 30, 15, 0,0)
        cluster8 = p.c.Cluster(set(["hl"]), 40, 13, 0,0)
        cluster_list = [cluster0, cluster1, cluster2, cluster3, cluster4, cluster5, cluster6, cluster7, cluster8]
        #print p.slow_closest_pair(cluster_list)
        self.assertEqual(p.slow_closest_pair(cluster_list), p.fast_closest_pair(cluster_list))


        #self.apoc_10 = Apocalypse(4,4,[],[(0,0)], [(0,1)])
        #self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
