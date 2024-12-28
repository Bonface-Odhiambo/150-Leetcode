def smaller_numbers_than_current(nums):
    # Create list of tuples with (number, original_index)
    indexed_nums = list(enumerate(nums))
    
    # Sort by the number, keeping track of original indices
    indexed_nums.sort(key=lambda x: x[1])
    
    result = [0] * len(nums)
    prev_num = float('-inf')
    count = 0
    
    # Iterate through sorted array
    for i, (orig_idx, num) in enumerate(indexed_nums):
        # If current number is different from previous
        # update the count of smaller numbers
        if num > prev_num:
            count = i
        # Store count at original index
        result[orig_idx] = count
        prev_num = num
    
    return result

# Test cases
test_cases = [
    [8, 1, 2, 2, 3],    # Example 1
    [6, 5, 4, 8],       # Example 2
    [7, 7, 7, 7]        # Example 3
]

for nums in test_cases:
    print(f"\nInput array: {nums}")
    result = smaller_numbers_than_current(nums)
    print(f"Numbers smaller than current: {result}")