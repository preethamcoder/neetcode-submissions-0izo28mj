import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, w in times:
            graph[s].append([w, d])
        seen = set()
        res = 0
        heap = [(0, k)]
        while heap:
            for ind in range(len(heap)):
                w1, n1 = heapq.heappop(heap)
                if n1 in seen:
                    continue
                seen.add(n1)
                res = max(res, w1)
                for w2, n2 in graph[n1]:
                    heapq.heappush(heap, (w2+w1, n2))
        return res if len(seen) == n else -1