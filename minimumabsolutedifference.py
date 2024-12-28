"""
Problem: Minimum Absolute Difference

Given an array of distinct integers arr
Find all pairs of elements with the minimum absolute difference of any two elements
Return a list of pairs in ascending order (with respect to pairs), each pair [a,b] follows:

a, b are from arr
a < b
b - a equals the minimum absolute difference of any two elements in arr



Examples:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1, and all pairs with difference 1 are shown in ascending order.
Input: arr = [1,3,6,10,15]
Output: [[3,6]]
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

Constraints:

2 <= arr.length <= 105
-106 <= arr[i] <= 106
All elements in arr are distinct
"""
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the array
        arr.sort()
        
        # Initialize variables
        min_diff = float('inf')
        result = []
        
        # Find minimum difference by comparing adjacent elements
        for i in range(len(arr) - 1):
            current_diff = arr[i + 1] - arr[i]
            
            # If we find a smaller difference
            if current_diff < min_diff:
                min_diff = current_diff
                result = [[arr[i], arr[i + 1]]]  # Reset result with new pair
            # If we find another pair with same minimum difference
            elif current_diff == min_diff:
                result.append([arr[i], arr[i + 1]])
        
        return result