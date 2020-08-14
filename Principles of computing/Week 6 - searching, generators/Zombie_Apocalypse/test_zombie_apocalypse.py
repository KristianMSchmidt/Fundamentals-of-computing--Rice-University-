import unittest

from zombie_apocalypse import Apocalypse
import zombie_apocalypse as zombie


class TestApocalypse(unittest.TestCase):


    def setUp(self):
        """
        Do the following after each test
        """
        #width,         height,obs_list, zombie_list, human_list
        self.apoc_1 = Apocalypse(5,5, [(1,1)], [(2,2)], [(4,4)])
        self.apoc_2 = Apocalypse(3,3, [(0,0)], [(1,1),(2,2)], [(0,1),(1,0),(1,1)])
        self.apoc_3 = Apocalypse(1,1, [],    [],           [])


    def tearDown(self):
        """
        Do the following after each test
        """
        pass

    def test_move_zombies(self):
        self.apoc_10 = Apocalypse(4,4,[],[(0,0)], [(0,1)])
        human_distance_field = self.apoc_10.compute_distance_field(zombie.HUMAN)
        self.apoc_10.move_zombies(human_distance_field)
        result = self.apoc_10._zombie_list
        expected = [(0,1)]
        self.assertEqual(result, expected)

    def test_move_zombies(self):
        self.apoc_11 = Apocalypse(4,4,[(0,1)],[(0,0)], [(2,2)])
        human_distance_field = self.apoc_11.compute_distance_field(zombie.HUMAN)
        self.apoc_11.move_zombies(human_distance_field)
        result = self.apoc_11._zombie_list
        expected = [(1,0)]
        self.assertEqual(result, expected)


    def test_move_zombies(self):
        self.apoc_11 = Apocalypse(4,4,[(0,1),(3,0)],[(0,0),(2,2),(3,1)], [(0,0),(2,0)])
        human_distance_field = self.apoc_11.compute_distance_field(zombie.HUMAN)
        self.apoc_11.move_zombies(human_distance_field)
        result = self.apoc_11._zombie_list
        expected = [(0,0),(2,1),(2,1)]
        self.assertEqual(result, expected)

    def test_move_humans(self):
        self.apoc_4 = Apocalypse(4,4,[],[(0,0)], [(0,1)])
        zombie_distance_field = self.apoc_4.compute_distance_field(zombie.ZOMBIE)
        self.apoc_4.move_humans(zombie_distance_field)
        result = self.apoc_4._human_list
        expected = [(1,2)]
        self.assertEqual(result, expected)

        self.apoc_5 = Apocalypse(4,4,[],[(0,0)], [(1,1)])
        zombie_distance_field = self.apoc_4.compute_distance_field(zombie.ZOMBIE)
        self.apoc_5.move_humans(zombie_distance_field)
        result = self.apoc_5._human_list
        possible_outcomes = [[(2,2)]]
        self.assertIn(result, possible_outcomes)

        self.apoc_6 = Apocalypse(4,4,[(2,2)],[(0,0)], [(1,1)])
        zombie_distance_field = self.apoc_4.compute_distance_field(zombie.ZOMBIE)
        self.apoc_6.move_humans(zombie_distance_field)
        result = self.apoc_6._human_list
        possible_outcomes = [[(1,2)],[(2,1)]]
        self.assertIn(result, possible_outcomes)

        self.apoc_7 = Apocalypse(4,4,[(2,2), (2,1)],[(0,0)], [(1,1),(2,3)])
        zombie_distance_field = self.apoc_4.compute_distance_field(zombie.ZOMBIE)
        self.apoc_7.move_humans(zombie_distance_field)
        result = self.apoc_7._human_list
        expected = [(1,2),(3,3)]
        self.assertEqual(result, expected)

        self.apoc_8 = Apocalypse(4,4,[(2,2), (2,1)],[(0,0),(3,3)], [(1,1),(2,3)])
        zombie_distance_field = self.apoc_8.compute_distance_field(zombie.ZOMBIE)
        self.apoc_8.move_humans(zombie_distance_field)
        result = self.apoc_8._human_list
        expected = [(1,2),(1,2)]
        self.assertEqual(result, expected)

        self.apoc_9 = Apocalypse(4,4,[(2,2), (2,1),(1,2),(0,2),(2,0)],[(0,0),(3,3)], [(1,1),(2,3)])
        zombie_distance_field = self.apoc_9.compute_distance_field(zombie.ZOMBIE)
        self.apoc_9.move_humans(zombie_distance_field)
        result = self.apoc_9._human_list
        expected = [(1,1),(1,3)]
        self.assertEqual(result, expected)


    def test_compute_distance_field(self):
        apoc_4 = Apocalypse(2,2,[],[],[])
        self.assertEqual(apoc_4.compute_distance_field(zombie.HUMAN), [[4,4],[4,4]])
        self.assertEqual(self.apoc_2.compute_distance_field(zombie.HUMAN), [[9,0,1],[0,0,1],[1,1,2]])
        apoc_5 = Apocalypse(3,3, [(0,0)], [(1,1),(2,2)], [(0,1),(1,0),(1,1)])
        self.assertEqual(apoc_5.compute_distance_field(zombie.ZOMBIE), [[9,1,2],[1,0,1],[2,1,0]])
        self.assertEqual(self.apoc_3.compute_distance_field(zombie.HUMAN), [[1]])

    def test_clear(self):
        self.apoc_1.clear()
        self.assertEqual(self.apoc_1._zombie_list, [])
        self.assertEqual(self.apoc_1._human_list, [])

    def test_num_zombies(self):
        self.assertEqual(self.apoc_1.num_zombies(),1)
        self.assertEqual(self.apoc_2.num_zombies(),2)
        self.assertEqual(self.apoc_3.num_zombies(),0)

    def test_add_zombie(self):
        self.apoc_1.add_zombie(3,4)
        self.assertEqual(self.apoc_1.num_zombies(),2)
        self.assertEqual(self.apoc_1._zombie_list, [(2,2),(3,4)])

    def test_num_humans(self):
        self.assertEqual(self.apoc_1.num_humans(),1)
        self.assertEqual(self.apoc_2.num_humans(),3)
        self.assertEqual(self.apoc_3.num_humans(),0)

    def test_add_human(self):
        self.apoc_1.add_human(3,4)
        self.assertEqual(self.apoc_1.num_humans(),2)
        self.assertEqual(self.apoc_1._human_list, [(4,4),(3,4)])

    def test_humans(self):
        yielding = []
        for human in self.apoc_1.humans():
            yielding.append(human)
        self.assertEqual(yielding, self.apoc_1._human_list)
        yielding = []
        for human in self.apoc_3.humans():
            yielding.append(human)
        self.assertEqual(yielding, self.apoc_3._human_list)

    def test_zombies(self):
        yielding = []
        for zombie in self.apoc_1.zombies():
            yielding.append(zombie)
        self.assertEqual(yielding, self.apoc_1._zombie_list)
        yielding = []
        for zombie in self.apoc_3.zombies():
            yielding.append(zombie)
        self.assertEqual(yielding, self.apoc_3._zombie_list)

if __name__ == '__main__':
    unittest.main()
