"""
3Sum Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:

i ≠ j, i ≠ k, and j ≠ k
nums[i] + nums[j] + nums[k] = 0
The solution set must not contain duplicate triplets

Examples from the image:
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: The distinct triplets are [-1,-1,2] and [-1,0,1]. Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraint:

3 ≤ nums.length ≤ 3000
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:  # Handle case with less than 3 numbers
            return []
            
        # Sort the array to handle duplicates and use two-pointer technique
        nums.sort()
        result = []
        
        # Iterate through the array except last two elements
        for i in range(len(nums)-2):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Two pointers technique
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
                    
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result