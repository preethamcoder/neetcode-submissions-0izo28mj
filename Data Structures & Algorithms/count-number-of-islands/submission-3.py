class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        seen = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in seen or grid[r][c] == '0':
                return
            seen.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        for x in range(rows):
            for y in range(cols):
                if (x, y) not in seen and grid[x][y] == '1':
                    dfs(x, y)
                    res += 1
        return res