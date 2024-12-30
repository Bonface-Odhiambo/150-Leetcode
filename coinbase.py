"""
Dynamic programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions. The next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution, thereby saving computation time. This technique of storing solutions to subproblems instead of recomputing them is called memoization.
Memoization is a technique used in computing to store the results of expensive function calls and return the cached result when the same inputs occur again. This technique can be used to speed up computations by storing the results of expensive function calls and returning the cached result when the same inputs occur again.
A greedy algorithm is an algorithmic paradigm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless, a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.
"""
class Solution:
    def coinChange(self, coins, amount): #coins is a list of coin values, amount is the target amount
        dp= [amount+1]*(amount+1) #initialize the dp array with amount+1
        dp[0]=0 #base case
        #array index
        for i in range(1, amount+1): #iterate through the dp array
            for c in coins: #iterate through the coins array
                    dp[i]= min(dp[i], dp[i-c]+1) #update the dp array
        return dp[amount] if dp[amount]!=amount+1 else -1 #return the result
solution = Solution()
# Time complexity: O(n*m) where n is the amount and m is the number of coins
# Test cases
print(solution.coinChange([1,2,5], 11))  # Output: 3
print(solution.coinChange([2], 3))       # Output: -1
print(solution.coinChange([1], 0))       # Output: 0