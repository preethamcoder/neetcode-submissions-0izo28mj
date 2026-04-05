class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        graph = {ind:[] for ind in range(length)}
        for ind in range(length):
            x1, y1 = points[ind]
            for ind2 in range(ind+1, length):
                x2, y2 = points[ind2]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[ind].append([dist, ind2])
                graph[ind2].append([dist, ind])
        seen = set()
        heap = [[0, 0]]
        res = 0
        while len(seen) < length:
            weight, node = heapq.heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            res += weight
            for each in graph[node]:
                w, n = each
                if n not in seen:
                    heapq.heappush(heap, [w, n])
        return res