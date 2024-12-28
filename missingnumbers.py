from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark indices as visited
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1  # Get the correct index
            if nums[temp] > 0:  # Mark as visited by making it negative
                nums[temp] *= -1

        # Collect numbers that are missing
        res = []
        for i, n in enumerate(nums):  # Use enumerate to get index and value
            if n > 0:  # If the number is positive, it means the index was not visited
                res.append(i + 1)

        return res

# Instantiate the class
solution = Solution()

# Sample input
nums = [4, 3, 2, 7, 8, 2, 3, 1]

# Run the function and print the result
missing_numbers = solution.findDisappearedNumbers(nums)
print("Missing numbers:", missing_numbers)
