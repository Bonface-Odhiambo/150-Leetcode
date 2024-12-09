def contains_duplicate_set (nums):
    """
    Checks for duplicates in a list using a set. Efficient for large data sets
    """
    seen=set()
    for num in nums:
        if num in seen:
            return True # when a duplicate was found
        seen.add(num) #No duplicates found
    return False
    
#Example Usage
nums1= [1,2,3,1]
nums2= [1,2,3,4]
print(contains_duplicate_set(nums1))
print(contains_duplicate_set(nums2))