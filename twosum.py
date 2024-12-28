def twosum(nums: list[int], target: int) ->list[int]:
    #Create a hash map to store the number -> index mapping
    hash_map= {}

    #iterate through the array
    for i, num in enumerate(nums):
        #Calculate the complement we need to find

        complement= target-num

        #if complement exists in the hash map, then we found our pair

        if complement in hash_map:
            return [hash_map[complement], i]
        
        # Add current number and its index to the map

        hash_map[num]=i

    return [] # no solution was found (though the problem guarantees that a solution exists)


# Example Usage 1
nums =[2,7,11,15]
target =9


# Result: [0,1] because nums [0]+ nums [1]= 2+7=9
#Example Usage 2
nums= [3,2,4]
target=6


#Result: [1,2] because nums[1]+ nums[2]= 2+4=6

#Example Usage 3

nums= [3,3]
target=6

#Result: [0,1] because nums[0]+nums [1]=3+3=6