#Here, we solve this problem using Depth-First-Search and recursion instead of iteration
from typing import List

class Islands:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i+1, j)  # down
            dfs(i-1, j)  # up
            dfs(i, j+1)  # right
            dfs(i, j-1)  # left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands

# Test cases
def test_numIslands():
    test_cases = [
        ([["1", "1", "0", "0", "0"],
          ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"],
          ["0", "0", "0", "1", "1"]], 3),  # Example 1
          
        ([["1", "0", "1", "0", "1"]], 3),  # Single row
        
        ([["1"], ["0"], ["1"], ["1"], ["0"]], 2),  # Single column
        
        ([["0", "0", "0"],
          ["0", "0", "0"],
          ["0", "0", "0"]], 0),  # No islands
        
        ([["1", "1"],
          ["1", "1"]], 1),  # All land
        
        ([], 0),  # Empty grid
        
        ([["1"]], 1),  # Single land cell
        
        ([["0"]], 0)   # Single water cell
    ]

    island = Islands()
    for i, (grid, expected) in enumerate(test_cases):
        result = island.numIslands([row[:] for row in grid])  # Copy grid to avoid mutation
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

if __name__ == '__main__':
    test_numIslands()
