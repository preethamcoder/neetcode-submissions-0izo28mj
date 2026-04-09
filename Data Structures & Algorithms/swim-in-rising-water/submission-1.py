import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        seen.add((0, 0))
        heap = [[grid[0][0], 0, 0]]
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        res = 0
        while heap:
            h, r, c = heapq.heappop(heap)
            res = max(res, h)
            if r == rows-1 and c == cols-1:
                return res
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in seen:
                    continue
                seen.add((row, col))
                heapq.heappush(heap, ([max(res, grid[row][col]), row, col]))
        return res