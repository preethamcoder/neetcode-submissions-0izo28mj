from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    q.append([x, y])
                elif grid[x][y] == 1:
                    fresh += 1
        while fresh > 0 and q:
            for ind in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        fresh -= 1
                        grid[row][col] = 2
                        q.append([row, col])
            time += 1
        return time if fresh == 0 else -1