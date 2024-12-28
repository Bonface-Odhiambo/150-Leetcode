class Solution:
    def lastFlowerPetals(self, flowers: int, nights: int) -> int:
        MOD = 10**9 + 7
        
        # For single flower, it will always have 1 petal
        if flowers == 1:
            return 1
            
        # For any number of flowers > 1
        # Last flower pattern: Each night adds the sum of all current petals
        # This creates an arithmetic sequence for the increments
        
        # Initial state: last flower has sum of all petals (all 1s)
        last_flower = flowers  # Sum of initial 1s
        increment = flowers    # Each night adds current sum
        
        # Calculate final petals after k nights
        for _ in range(nights):
            last_flower = (last_flower + increment) % MOD
            increment = (increment + flowers) % MOD
            
        return last_flower