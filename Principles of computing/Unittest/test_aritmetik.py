#standardbiblioteket
#https://docs.python.org/2/library/unittest.html

#Fremgangsmaaden i TDD (test driven development)
# 1. Think           (DESIGN AND TESTING IN ONE)
# 2. Write test     (DESIGN AND TESTING IN ONE)
# 3. Make test fail
# 4. Implement so that the test passes
# 5. Run all unittests and fix failures
# 6. Refactor your code (make it elegant, efficient and pretty)
# 7. Run all unittests and fix failures
# 8. Check in your code (??)

import unittest
import aritmetik

from aritmetik import multiply
#from aritmetik import * Dette virker og goer testkoden kortere. Men er det god skik???

class TestAritmetik(unittest.TestCase):

    def test_basic(self):
        result = 2
        expected = 2
        self.assertEqual(result,expected)

    def test_add(self):
        self.assertEqual(aritmetik.add(3,4),7)
        self.assertEqual(aritmetik.add(-1,-1),-2)

    def test_multiply(self):
        self.assertEqual(multiply(2,3),6)
        self.assertEqual(aritmetik.multiply(2.5,2.5), 6.25)


if __name__ == '__main__':
    unittest.main()
