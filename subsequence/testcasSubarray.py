#! /usr/bin/python3
import unittest
from parameterized import parameterized
from subarray import findsubarray


class TestSubarray(unittest.TestCase):
    @parameterized.expand([
        [True, [2,3,4], [2,3]],
        [True, [3,3,4], [3,3]],
        [False, [2,5,6], [2,5,6,3]],
        [False, ["ai","fu",3,4], [3,"fu"]],
        [True, ["a","b"], ["a"]],
        [False, [2,3,4], [4,3]],

    ])

    def test_cases(self,expected,first_array,second_array):
        result=findsubarray(first_array,second_array)
        self.assertEqual(result,expected)



if __name__ == '__main__':
    unittest.main()
