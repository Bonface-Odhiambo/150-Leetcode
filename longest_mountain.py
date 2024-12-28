from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # Handle base case
        if len(arr) < 3:
            return 0
            
        n = len(arr)
        max_length = 0
        
        # Check each potential peak
        for i in range(1, n-1):
            # Skip if not a peak
            if arr[i] <= arr[i-1] or arr[i] <= arr[i+1]:
                continue
                
            # Found potential peak, expand left
            left = i
            while left > 0 and arr[left-1] < arr[left]:
                left -= 1
                
            # Expand right
            right = i
            while right < n-1 and arr[right] > arr[right+1]:
                right += 1
                
            # Calculate current mountain length
            current_length = right - left + 1
            
            # Update max_length if we found a valid mountain
            if current_length >= 3:
                max_length = max(max_length, current_length)
        
        return max_length