import unittest
from typing import List
from solution import Solution

class TestLongestMountain(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        """Test the first example from the problem"""
        arr = [2,1,4,7,3,2,5]
        expected = 5
        self.assertEqual(self.solution.longestMountain(arr), expected)
    
    def test_example2(self):
        """Test the second example with no mountain"""
        arr = [2,2,2]
        expected = 0
        self.assertEqual(self.solution.longestMountain(arr), expected)
        
    def test_too_short(self):
        """Test array with length less than 3"""
        arr = [1,2]
        expected = 0
        self.assertEqual(self.solution.longestMountain(arr), expected)
    
    def test_no_peak(self):
        """Test array with no peak"""
        arr = [1,2,3,4,5]
        expected = 0
        self.assertEqual(self.solution.longestMountain(arr), expected)
    
    def test_multiple_mountains(self):
        """Test array with multiple mountains"""
        arr = [1,2,3,2,1,4,5,2,1]
        expected = 5
        self.assertEqual(self.solution.longestMountain(arr), expected)
        
    def test_edge_peak(self):
        """Test array with peak at edges"""
        arr = [5,4,3,2,1]  # Descending only
        expected = 0
        self.assertEqual(self.solution.longestMountain(arr), expected)

if __name__ == '__main__':
    unittest.main()