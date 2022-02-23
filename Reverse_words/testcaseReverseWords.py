#! /usr/bin/python3
import unittest
from parameterized import parameterized
from reversewords import reverse_word


class TestReverseWords(unittest.TestCase):
    @parameterized.expand([
        ["yM emaN si asseJ", "My Name is Jessa"],


    ])

    def test_cases(self,expected,string):
        result=reverse_word(string)
        self.assertEqual(result,expected)



if __name__ == '__main__':
    unittest.main()
