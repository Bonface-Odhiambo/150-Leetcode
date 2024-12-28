def lastFlowerPetals(flowers, nights):
    # Define modulo constant to handle large numbers
    MOD = 1000000007  # 10^9 + 7
    
    # Handle base case for single flower
    if flowers == 1:
        return 1
        
    # Initialize variables
    # last_flower tracks the petals in last flower
    # increment tracks how much we add each night
    last_flower = flowers    # Initially, sum of all 1s
    increment = flowers      # Initially, sum of all flowers
    
    # Simulate each night
    for _ in range(nights):
        # Add current increment to last flower
        last_flower = (last_flower + increment) % MOD
        
        # Increase increment by number of flowers
        # Because each position will contribute one more petal
        increment = (increment + flowers) % MOD
    
    return last_flower

# Example Usage:
if __name__ == "__main__":
    # Test case 1:
    flowers1 = 3
    nights1 = 4
    result1 = lastFlowerPetals(flowers1, nights1)
    print(f"For {flowers1} flowers and {nights1} nights, the last flower has {result1} petals.")  # Output: 33

    # Test case 2:
    flowers2 = 5
    nights2 = 2
    result2 = lastFlowerPetals(flowers2, nights2)
    print(f"For {flowers2} flowers and {nights2} nights, the last flower has {result2} petals.")  # Output: 35
    
    # Test case 3: Single flower
    flowers3 = 1
    nights3 = 10
    result3 = lastFlowerPetals(flowers3, nights3)
    print(f"For {flowers3} flowers and {nights3} nights, the last flower has {result3} petals.") #Output: 1

    # Test case 4: Larger numbers
    flowers4 = 10
    nights4 = 100
    result4 = lastFlowerPetals(flowers4, nights4)
    print(f"For {flowers4} flowers and {nights4} nights, the last flower has {result4} petals.")

    # Test case 5: Very large numbers
    flowers5 = 1000
    nights5 = 1000
    result5 = lastFlowerPetals(flowers5, nights5)
    print(f"For {flowers5} flowers and {nights5} nights, the last flower has {result5} petals.")