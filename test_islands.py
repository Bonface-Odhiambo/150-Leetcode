import unittest
from typing import List

# Main class containing the numIslands method
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

# Unit tests for the numIslands method
class TestIslands(unittest.TestCase):
    def setUp(self):
        self.islands = Islands()

    def test_example_case(self):
        grid = [["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]]
        self.assertEqual(self.islands.numIslands([row[:] for row in grid]), 3)

    def test_single_row(self):
        grid = [["1", "0", "1", "0", "1"]]
        self.assertEqual(self.islands.numIslands([row[:] for row in grid]), 3)

    def test_single_column(self):
        grid = [["1"], ["0"], ["1"], ["1"], ["0"]]
        self.assertEqual(self.islands.numIslands([row[:] for row in grid]), 2)

    def test_no_islands(self):
        grid = [["0", "0", "0"],
                ["0", "0", "0"],
                ["0", "0", "0"]]
        self.assertEqual(self.islands.numIslands([row[:] for row in grid]), 0)

    def test_all_land(self):
        grid = [["1", "1"],
                ["1", "1"]]
        self.assertEqual(self.islands.numIslands([row[:] for row in grid]), 1)

    def test_empty_grid(self):
        grid = []
        self.assertEqual(self.islands.numIslands(grid), 0)

    def test_single_land_cell(self):
        grid = [["1"]]
        self.assertEqual(self.islands.numIslands([row[:] for row in grid]), 1)

    def test_single_water_cell(self):
        grid = [["0"]]
        self.assertEqual(self.islands.numIslands([row[:] for row in grid]), 0)

# Run the tests from the terminal
if __name__ == '__main__':
    unittest.main()
