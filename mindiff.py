from typing import List

def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    # Sort the array
    arr.sort()
    
    # Initialize variables
    min_diff = float('inf')
    result = []
    
    # Find minimum difference
    for i in range(len(arr) - 1):
        curr_diff = arr[i + 1] - arr[i]
        if curr_diff < min_diff:
            min_diff = curr_diff
            result = [[arr[i], arr[i + 1]]]
        elif curr_diff == min_diff:
            result.append([arr[i], arr[i + 1]])
    
    return result