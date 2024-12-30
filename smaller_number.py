def smaller_numbers_than_current(nums): # nums is the input array
    n= len(nums) # nums are the individual elements in the array
    result= [0]* n

    for i in range (n):
        count =0
        for j in range(n):
            if i!= j and nums[j]<nums[i]:
                count+=1
        result[i]=count
    return result

#Example usage

test_cases= [[8,1,2,2,3], # Example 1
             [6,5,4,8], # Example 2
             [7,7,7,7] # Example 3
             ]
for nums in test_cases:
    print(f"\nInput array: {nums}")
    print(f"Brute force solution: {smaller_numbers_than_current(nums)}")
