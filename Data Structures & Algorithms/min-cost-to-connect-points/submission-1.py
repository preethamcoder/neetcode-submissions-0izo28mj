import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        heap = [(0, 0)]
        seen = set()
        res = 0
        length = len(points)
        for ind in range(length):
            x1, y1 = points[ind]
            for ind2 in range(ind+1, length):
                x2, y2 = points[ind2]
                dist = abs(x2-x1) + abs(y2-y1)
                graph[ind].append([dist, ind2])
                graph[ind2].append([dist, ind])
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in seen:
                continue
            seen.add(n1)
            res += w1
            for w2, n2 in graph[n1]:
                if n2 not in seen:
                    heapq.heappush(heap, (w2, n2))
        return res