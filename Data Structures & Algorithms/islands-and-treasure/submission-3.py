from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        seen = set()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    seen.add((x, y))
                    q.append([x, y])
        def add_cell(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in seen or grid[r][c] == -1:
                return
            seen.add((r, c))
            q.append([r, c])
        curr_dist = 0
        while q:
            for ind in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = curr_dist
                add_cell(r+1, c)
                add_cell(r-1, c)
                add_cell(r, c+1)
                add_cell(r, c-1)
            curr_dist += 1
