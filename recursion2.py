#Another instance of recursion is when an algorithm needs one base case to prevention infite recursion
def dfs(i, j):
    if (i < 0 or i >= rows or 
        j < 0 or j >= cols or 
        grid[i][j] != '1'):
        return  # This is the base case

"""
Progress Toward Base Case
Each recursive call should move closer to the base case. In the islands example:


Each call marks a '1' as '0'
Eventually, all connected land cells will be marked as water
When no more '1's are adjacent, we hit the base case
"""