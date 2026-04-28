class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for ind in range(1, cols):
            grid[0][ind] += grid[0][ind-1]
        for ind in range(1, rows):
            grid[ind][0] += grid[ind-1][0]
        for ind in range(1, rows):
            for ind2 in range(1, cols):
                grid[ind][ind2] += min(grid[ind-1][ind2], grid[ind][ind2-1])
        return grid[-1][-1]