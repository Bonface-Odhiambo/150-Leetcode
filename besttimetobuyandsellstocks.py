"""
Problem Statement:
You are given an array prices where prices[i] represents the price of a stock on the 
ith day.
You need to maximize your profit by choosing:
A single day to buy the stock, and
A different day in the future to sell the stock.
The goal is to calculate and return the maximum profit you can achieve.
If no profit can be made, return 0.
"""
from typing import List

def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1  # Left pointer (buy day), right pointer (sell day)
    maxP = 0     # Initialize max profit
    
    while r < len(prices):  # Traverse the list until the end
        if prices[l] < prices[r]:  # Check if the current window is profitable
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)  # Update max profit
        else:
            l = r  # Move the left pointer to the right pointer if no profit
        
        r += 1  # Move the right pointer forward
    
    return maxP

# Test Cases
prices1 = [7, 1, 5, 3, 6, 4]  # Output: 5
prices2 = [7, 6, 4, 3, 1]     # Output: 0
prices3 = [2, 4, 1, 7, 5, 9]  # Output: 8
prices4 = [3, 3, 3, 3]        # Output: 0
prices5 = [1, 2, 3, 4, 5]     # Output: 4

# Collect all results in a list
results = [
    maxProfit(prices1),
    maxProfit(prices2),
    maxProfit(prices3),
    maxProfit(prices4),
    maxProfit(prices5)
]

# Print all results at once
print(results)
