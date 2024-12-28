def smaller_numbers_than_current(nums):
    # Sort the nums array to find ranks
    temp = sorted(nums)  # temp = sorted version of nums
    d = {}  # Dictionary to store ranks

    # Populate the dictionary with the smallest rank of each number
    for i, num in enumerate(temp):
        if num not in d:  # Assign rank only if the number is not already in the dictionary
            d[num] = i

    # Construct the result array using the dictionary
    ret = []
    for i in nums:
        ret.append(d[i])  # Append the rank of each number from the original array

    return ret


# Explanation of the approach:
"""
In this solution, it is significant to remember that:
- Time complexity is more important than space complexity.
- Sorting the array (O(n log n)) allows us to determine the ranks efficiently.
- Space is used to store the dictionary, but this trade-off is acceptable for faster run time.
-Space is cheap and so we focus on time complexity
"""

# Example test cases
test_cases = [
    [8, 1, 2, 2, 3],  # Example 1
    [6, 5, 4, 2],     # Example 2
    [7, 7, 7, 7]      # Example 3
]

# Run the function on each test case
for nums in test_cases:
    print(f"Input array: {nums}")
    print(f"Optimized solution: {smaller_numbers_than_current(nums)}")
"""
Time Complexity
Sorting: 
𝑂(𝑛log𝑛)
O(nlogn)
Dictionary Construction: 
𝑂(𝑛)
O(n)
Result Construction: 
𝑂(𝑛)
O(n)
Overall: 
𝑂(𝑛log𝑛)
O(nlogn)
This approach is significantly more efficient than the brute-force 
𝑂(𝑛2)
O(n2) solution.
 """