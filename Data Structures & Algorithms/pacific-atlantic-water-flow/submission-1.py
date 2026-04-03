class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        res = []
        pac = set()
        atl = set()
        def dfs(r, c, visited, prev_h):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prev_h:
                return
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
        for each in range(rows):
            dfs(each, 0, pac, heights[each][0])
            dfs(each, cols-1, atl, heights[each][cols-1])
        for each in range(cols):
            dfs(0, each, pac, heights[0][each])
            dfs(rows-1, each, atl, heights[rows-1][each])
        for each in pac:
            if each in atl:
                res.append(each)
        return res