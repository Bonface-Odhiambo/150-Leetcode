import unittest
from solution import Solution

class TestMagicalGarden(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        """Test the first example from the problem"""
        flowers = 3
        nights = 4
        expected = 15
        self.assertEqual(self.solution.lastFlowerPetals(flowers, nights), expected)
    
    def test_example2(self):
        """Test the second example from the problem"""
        flowers = 2
        nights = 5
        expected = 6
        self.assertEqual(self.solution.lastFlowerPetals(flowers, nights), expected)
    
    def test_single_flower(self):
        """Test with single flower - should always remain 1"""
        flowers = 1
        nights = 100
        expected = 1
        self.assertEqual(self.solution.lastFlowerPetals(flowers, nights), expected)
    
    def test_zero_nights(self):
        """Test with zero nights - should return initial sum"""
        flowers = 4
        nights = 0
        expected = 4  # Initial state: sum of all 1s
        self.assertEqual(self.solution.lastFlowerPetals(flowers, nights), expected)
    
    def test_large_numbers(self):
        """Test with large numbers to verify modulo works"""
        flowers = 1000
        nights = 1000
        result = self.solution.lastFlowerPetals(flowers, nights)
        self.assertTrue(0 <= result < 10**9 + 7)
    
    def test_pattern_verification(self):
        """Test to verify the pattern for a specific case"""
        flowers = 3
        nights = 3
        expected = 10  # [1,4,10] after 3 nights
        self.assertEqual(self.solution.lastFlowerPetals(flowers, nights), expected)

if __name__ == '__main__':
    unittest.main()