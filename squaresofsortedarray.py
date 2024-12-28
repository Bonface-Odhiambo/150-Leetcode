"""
You are given an integer array nums sorted in non-decreasing order. Return an array of the squares of each number sorted in non-decreasing order.
"""

"""
In this solution, we are using a sorting approach.
Args:
    Iterating through the list gives a run time of (O(n))
    The sort function gives O(n(log)n)
Returns:
    The list of numbers in the array in ascending order
"""
from typing import List

class Solution(object):
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sq_list = [num**2 for num in nums]
        sq_list.sort()
        return sq_list

# List of test cases
test_cases = [
    [-4, -1, 0, 3, 10],
    [-3, -2, -1, 0, 2, 4],
    [-5, -4, -3, -1, 2, 3, 4]
]

solution = Solution()

# Loop through each test case and print the result
for test_case in test_cases:
    print(solution.sortedSquares(test_case))
