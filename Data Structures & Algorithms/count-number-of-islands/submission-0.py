class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        seen = set()

        def dfs(g, r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in seen or g[r][c] == '0':
                return
            seen.add((r, c))
            dfs(g, r+1, c)
            dfs(g, r-1, c)
            dfs(g, r, c-1)
            dfs(g, r, c+1)
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] != '0' and (x, y) not in seen:
                    dfs(grid, x, y)
                    res += 1
        return res