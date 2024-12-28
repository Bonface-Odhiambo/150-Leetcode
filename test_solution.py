import unittest
from typing import List
from solution import Solution

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        """Test the first example from the problem"""
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = self.solution.threeSum(nums)
        # Sort both result and expected for comparison
        sorted_result = sorted([sorted(x) for x in result])
        sorted_expected = sorted([sorted(x) for x in expected])
        self.assertEqual(sorted_result, sorted_expected)
    
    def test_example2(self):
        """Test the second example with no solution"""
        nums = [0, 1, 1]
        expected = []
        self.assertEqual(self.solution.threeSum(nums), expected)
    
    def test_example3(self):
        """Test the third example with all zeros"""
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        result = self.solution.threeSum(nums)
        sorted_result = sorted([sorted(x) for x in result])
        sorted_expected = sorted([sorted(x) for x in expected])
        self.assertEqual(sorted_result, sorted_expected)

if __name__ == '__main__':
    unittest.main()