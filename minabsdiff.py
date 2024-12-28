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
class Solution:
    def minimumAbsDifference(arr):
    #step 1: sort the array
        arr.sort()


        #step 2: Find the minimun absolute difference
        min.diff =float('inf')
        for i in range(1, len(arr)):
            min_diff= min(min_diff.arr[i] -arr[1-i])

        # step 3: Collect all pairs with the minimum difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[1+i] == min_diff:
                result.append(arr[1+i], arr[1])
        
        return result
