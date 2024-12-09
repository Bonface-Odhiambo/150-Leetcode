def contains_duplicate_nested_loops(nums):
    """
    Checks for duplicates in a list. 
    Inefficient because 
    the loop operation has to run multiple times to find whether there are diplicates
    """
    n= len(nums)
    for i in range (n):
        for j in range(i+1, n):
            if nums[i] == nums[j]: 
                return True
        return False

#Example Usage
nums1= [1,2,3,1]
nums2= [1,2,3,4]
print(contains_duplicate_nested_loops(nums1))
print(contains_duplicate_nested_loops(nums2))
