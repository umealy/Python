#! /usr/bin/python3
import unittest
from parameterized import parameterized
from LinearSearch import linearSearch


class TestLinearSearch(unittest.TestCase):
    @parameterized.expand([
        [1, [2,3,4], 3],
        [None,[5,6], 9],
        [2, [2,3,4], 4],

    ])

    def test_cases(self,expected,array,element):
        result=linearSearch(array,element)
        self.assertEqual(result,expected)



if __name__ == '__main__':
    unittest.main()
