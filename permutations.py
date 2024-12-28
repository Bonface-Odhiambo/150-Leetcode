from typing import List

def min_operations_to_permutation(arr: List[int]) -> int:
    """
    Calculates the minimum number of operations to transform an array into a permutation of 1 to N.
    
    Args:
        arr: A list of integers.
    
    Returns:
        The minimum number of operations required.
    """
    n = len(arr)
    operations = 0
    
    # Count frequencies and track positions
    freq = {}
    positions = {}
    for i, num in enumerate(arr):
        freq[num] = freq.get(num, 0) + 1
        if num not in positions:
            positions[num] = []
        positions[num].append(i)
    
    # Handle duplicates and missing numbers
    duplicates = []  # Positions that need to be filled
    missing = []    # Numbers that need to be placed
    
    for i in range(1, n + 1):
        if i not in freq:
            missing.append(i)
        else:
            # For numbers appearing more than once
            while freq[i] > 1:
                # Find position furthest from its ideal position
                max_diff = -1
                max_pos = -1
                for pos in positions[i]:
                    diff = abs(pos + 1 - i)
                    if diff > max_diff:
                        max_diff = diff
                        max_pos = pos
                
                duplicates.append(max_pos)
                positions[i].remove(max_pos)
                freq[i] -= 1
    
    # Calculate operations for non-duplicate numbers
    for num, pos_list in positions.items():
        if num in freq and freq[num] == 1:
            operations += abs(pos_list[0] + 1 - num)
    
    # Match duplicates positions with missing numbers optimally
    duplicates.sort()
    missing.sort()
    for i in range(len(duplicates)):
        operations += abs(duplicates[i] + 1 - missing[i])
    
    return operations


# DO NOT CHANGE the code below, we use it to grade your submission. If changed your submission will be failed automatically.
if __name__ == '__main__':  
    line = input()
    k = [int(i) for i in line.strip().split()]
    print(min_operations_to_permutation(k))
test_cases = [
    [1, 1, 1],              # All same numbers
    [2, 1],                 # Simple swap
    [1, 2, 3],             # Already a permutation
    [3, 3, 3, 3],          # All duplicates
    [4, 1, 4, 2],          # Multiple duplicates
    [2, 2, 1, 1, 3],       # Multiple pairs of duplicates
    [5, 4, 3, 2, 1],       # Reversed permutation
    [1, 1, 2, 2, 3, 3]     # Alternating duplicates
]

def test_function(test_cases):
    for i, case in enumerate(test_cases):
        result = min_operations_to_permutation(case)
        print(f"Test case {i + 1}: {case}")
        print(f"Result: {result}")
        print("-" * 40)

test_function(test_cases)