class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        res = []
        def dfs(r, c, visit, prevH):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or heights[r][c] < prevH:
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
        for each in range(rows):
            dfs(each, 0, pac, heights[each][0])
            dfs(each, cols-1, atl, heights[each][cols-1])
        for each in range(cols):
            dfs(0, each, pac, heights[0][each])
            dfs(rows-1, each, atl, heights[rows-1][each])
        for each in atl:
            if each in pac:
                res.append(each)
        return res