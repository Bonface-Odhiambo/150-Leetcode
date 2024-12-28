"""
You are given an integer array nums sorted in non-decreasing order. Return an array of the squares of each number sorted in non-decreasing order.
"""

"""
In this solution, we are using a split and merge solution.
Args:
    First, we find index 0 (loop O(N))
    Second, we reverse negatives to 0 (O(N))
    Third, we square and merge (O(N))
Returns:
    The list of numbers in the array in ascending order
"""
def sortedSquares(nums):
    # Edge case: Empty array
    if not nums:
        return nums
    
    # If the first number is positive, just square all elements
    if nums[0] > 0:
        return [num**2 for num in nums]
    
    # Find the index of the first positive number
    m = 0
    for i, n in enumerate(nums):
        if n > 0:
            m = i
            break

    # A = positive numbers, B = reversed negatives
    A = nums[m:]  # Positive numbers
    B = [n for n in reversed(nums[:m])]  # Reversed negative numbers
    
    # Merge the two lists A and B
    def merge(A, B):
        ret = []
        i, j = 0, 0  # Use indices for A and B

        # Merge two sorted lists
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                ret.append(A[i])
                i += 1
            else:
                ret.append(B[j])
                j += 1
        
        # If any elements remain in A or B, append them
        if i < len(A):
            ret.extend(A[i:])
        if j < len(B):
            ret.extend(B[j:])
        
        # Square the merged list before returning
        return [n**2 for n in ret]

    # Call merge and return the result
    return merge(A, B)

# Test cases
print(sortedSquares([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]
print(sortedSquares([-3, -2, -1, 0, 2, 4]))  # Output: [0, 1, 4, 4, 9, 16]
print(sortedSquares([-5, -4, -3, -1, 2, 3, 4]))  # Output: [1, 4, 9, 9, 16, 16, 25]
