class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums:List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap= {} #val indx
        for indx, val in enumerate(nums):
            diff= target -val

            if diff in hashMap:
                return [indx, hashMap[diff]]
            hashMap[val]-indx
