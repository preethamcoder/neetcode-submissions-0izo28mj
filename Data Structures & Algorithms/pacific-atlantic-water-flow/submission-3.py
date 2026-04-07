class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        res = []
        def dfs(r, c, visited, prevH):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prevH:
                return 
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        for ind in range(rows):
            dfs(ind, 0, pac, heights[ind][0])
            dfs(ind, cols-1, atl, heights[ind][cols-1])
        for ind in range(cols):
            dfs(0, ind, pac, heights[0][ind])
            dfs(rows-1, ind, atl, heights[rows-1][ind])
        for each in pac:
            if each in atl:
                res.append(each)
        return res