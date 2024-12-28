"""
You are given an integer array nums sorted in non-decreasing order. Return an array of the squares of each number sorted in non-decreasing order.
"""

"""
In this solution, we are using absolute and merge. 
Args:
    First, we iterate through the list O(N)
    Second, we append to deque (O(1))
Returns:
    The list of numbers in the array in ascending order
"""
import collections

def sortedSquares(A):
    answer = collections.deque()
    l, r = 0, len(A) - 1

    # Compare the squares of the left and right elements
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left ** 2)  # Append square of left
            l += 1
        else:
            answer.appendleft(right ** 2)  # Append square of right
            r -= 1

    # Convert deque to list and return it
    return list(answer)

# Test cases
print(sortedSquares([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]
print(sortedSquares([-3, -2, -1, 0, 2, 4]))  # Output: [0, 1, 4, 4, 9, 16]
print(sortedSquares([-5, -4, -3, -1, 2, 3, 4]))  # Output: [1, 4, 9, 9, 16, 16, 25]
