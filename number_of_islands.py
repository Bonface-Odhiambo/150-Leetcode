#Problem Statement:Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are surrounded by water.

"""
One solution is a brute force algorithm with an iteration over the matrix
We will use breadth first search- It traverses through one level of children nodes then traverses through the level of grandchildren nodes and so on...These algorithms are either iterative or recursive.
Recursive algorithms are harder to read and debug and can take up a lot of space which implies they have a larger space complexity.
This means recursive algorithms can cause stack overflow causing one to run out of memory
It is recommended to use an iterative approach in this case.
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Corner case 1: Empty grid
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        # Corner case 2: Invalid input validation
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] not in ['0', '1']:
                    raise ValueError("Grid should only contain '0' or '1'")

        def is_valid(i: int, j: int) -> bool:
            # Corner case 3: Boundary check
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            # Corner case 4: Already visited or water
            if grid[i][j] != '1':
                return False
            return True

        def dfs(i: int, j: int) -> None:
            # Corner case 5: Invalid starting point
            if not is_valid(i, j):
                return

            # Mark as visited
            grid[i][j] = '2'  # Using '2' instead of '0' to distinguish visited cells

            # Check all 4 directions
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in directions:
                next_i, next_j = i + di, j + dj
                dfs(next_i, next_j)

        # Main logic
        try:
            for i in range(rows):
                for j in range(cols):
                    # Corner case 6: Skip water and visited cells
                    if grid[i][j] == '1':
                        islands += 1
                        dfs(i, j)
            return islands

        # Corner case 7: Handle any runtime errors
        except Exception as e:
            raise RuntimeError(f"Error processing grid: {str(e)}")


if __name__ == '__main__':
    grid = [["1", "1", "1", "0"],
            ["1", "1", "0", "0"],
            ["1", "1", "0", "0"],
            ["0", "0", "0", "0"]]
    solution = Solution()
    print(solution.numIslands(grid))



