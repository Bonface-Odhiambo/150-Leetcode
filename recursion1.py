# One instance of recursion is when a function calls itself as in this case
def dfs(i, j):
    # ... some code ...
    dfs(i+1, j)  # Function calls itself with different parameters
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)