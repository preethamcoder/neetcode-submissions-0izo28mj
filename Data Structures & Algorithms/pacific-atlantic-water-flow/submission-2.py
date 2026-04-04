class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows = len(heights)
        cols = len(heights[0])
        res = []
        def dfs(r, c, visited, prevH):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prevH:
                return 
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        for x in range(rows):
            dfs(x, 0, pac, heights[x][0])
            dfs(x, cols-1, atl, heights[x][cols-1])
        for y in range(cols):
            dfs(0, y, pac, heights[0][y])
            dfs(rows-1, y, atl, heights[rows-1][y])
        for each in pac:
            if each in atl:
                res.append(each)
        return res