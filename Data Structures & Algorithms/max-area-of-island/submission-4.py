class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        res = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r, c))
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and (x, y) not in seen:
                    res = max(res, dfs(x, y))
        return res