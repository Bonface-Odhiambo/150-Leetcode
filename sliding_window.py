"""
Problem: Contains Duplicate II

Given an integer array nums and an integer k
Return true if there are two distinct indices i and j in the array such that:

nums[i] == nums[j]
abs(i - j) <= k


Return false otherwise

Examples:

Input: nums = [1,2,3,1], k = 3
Output: true
Explanation: nums[0] = nums[3] and abs(0 - 3) = 3
Input: nums = [1,0,1,1], k = 1
Output: true
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store number and its most recent index
        num_indices = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if number exists and distance is <= k
            if num in num_indices and i - num_indices[num] <= k:
                return True
                
            # Update/Add the most recent index for current number
            num_indices[num] = i
            
        return False


