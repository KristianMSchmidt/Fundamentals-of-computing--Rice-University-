import unittest

import wrangler

class TestWrangler(unittest.TestCase):

    def setUp(self):
        """
        Do the following after each test
        """
        self.list1=[]
        self.list2=[0]
        self.list3=[1,1]
        self.list4=[1,1,1]
        self.list5=[1,2,3,3,3,4,5,5,5,5]
        self.list6=[1,2,3,4]
        self.list7 =[-1,-1,0,1,1,2]

    def tearDown(self):
        """
        Do the following after each test
        """
        pass

    def test_gen_all_strings(self):
        result1 = sorted(wrangler.gen_all_strings("aab"))
        expected1 = sorted(["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"])
        self.assertEqual(result1, expected1)

        result2 = sorted(wrangler.gen_all_strings(""))
        expected2 = sorted([""])
        self.assertEqual(result2, expected2)

        result3 = sorted(wrangler.gen_all_strings("a"))
        expected3 = sorted(["", "a"])
        self.assertEqual(result3, expected3)

    def test_remove_dublicates(self):
        self.assertEqual(wrangler.remove_duplicates(self.list1), [])
        self.assertEqual(wrangler.remove_duplicates(self.list2), [0])
        self.assertEqual(wrangler.remove_duplicates(self.list3), [1])
        self.assertEqual(wrangler.remove_duplicates(self.list4), [1])
        self.assertEqual(wrangler.remove_duplicates(self.list5), [1,2,3,4,5])
        self.assertEqual(wrangler.remove_duplicates(self.list6), [1,2,3,4])

    def test_intersect(self):
        self.assertEqual(wrangler.intersect(self.list1,self.list1), [])
        self.assertEqual(wrangler.intersect(self.list1,self.list2), [])
        self.assertEqual(wrangler.intersect(self.list2,self.list3), [])
        self.assertEqual(wrangler.intersect(self.list3,self.list4), [1,1])
        self.assertEqual(wrangler.intersect(self.list4,self.list5), [1])
        self.assertEqual(wrangler.intersect(self.list5,self.list6), [1,2,3,4])
        self.assertEqual(wrangler.intersect(self.list6,self.list7), [1,2])


    def test_merge(self):
        self.assertEqual(wrangler.merge(self.list1, self.list1), [])
        self.assertEqual(wrangler.merge(self.list2, self.list1), [0])
        self.assertEqual(wrangler.merge(self.list2, self.list3), [0,1,1])
        self.assertEqual(wrangler.merge(self.list3, self.list3), [1,1,1,1])
        self.assertEqual(wrangler.merge(self.list3, self.list4), [1,1,1,1,1])
        self.assertEqual(wrangler.merge(self.list4, self.list5), [1,1,1,1,2,3,3,3,4,5,5,5,5])
        self.assertEqual(wrangler.merge(self.list5, self.list6), [1,1,2,2,3,3,3,3,4,4,5,5,5,5])

    def test_merge_sort(self):
        self.assertEqual(wrangler.merge_sort(self.list1), self.list1)
        self.assertEqual(wrangler.merge_sort(self.list2), self.list2)
        self.assertEqual(wrangler.merge_sort(self.list2), self.list2)
        self.assertEqual(wrangler.merge_sort(self.list3), self.list3)
        self.assertEqual(wrangler.merge_sort(self.list4), self.list4)
        self.assertEqual(wrangler.merge_sort(self.list5), self.list5)
        self.assertEqual(wrangler.merge_sort([9,8,7]), [7,8,9])
        self.assertEqual(wrangler.merge_sort([1,0]), [0,1])
        self.assertEqual(wrangler.merge_sort([9,8,8,9,4]), [4,8,8,9,9])
        self.assertEqual(wrangler.merge_sort([4,4,4,4,3,4]),[3,4,4,4,4,4])


if __name__ == '__main__':
    unittest.main()
