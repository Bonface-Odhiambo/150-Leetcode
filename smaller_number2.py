def efficient_smaller_numbers_than_current(nums):
    #count frequency of each number
    count= [0] * 102 # assuming the numbers <=100
    for num in nums:
        count[num] +=1


    #calculate running sum
    for i in range(1, 102):
        count[i] +=count[i-1]
    
    result = [0] * len(nums)
    for i in range(len(nums)):
        if nums[i] ==0:
            result[i] =0
        else:
            result[i] = count[nums[i]-1]
        return result

# Example Usage

test_cases= [[8,1,2,2,3], # Example from image 1
             [6,5,4,8], # Example from image 2
             [7,7,7,7] # Example from image 3
             ]
for nums in test_cases:
    print(f"\nInput array: {nums}")
    print(f"Efficient solution: {efficient_smaller_numbers_than_current(nums)}")
    
