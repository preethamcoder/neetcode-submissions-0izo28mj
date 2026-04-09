import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, v, w in times:
            graph[s].append([w, v])
        seen = set()
        heap = [(0, k)]
        res = 0
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in seen:
                continue
            seen.add(n1)
            res = max(res, w1)
            for w2, n2 in graph[n1]:
                if n2 not in seen:
                    heapq.heappush(heap, (w1+w2, n2))
        return res if len(seen) == n else -1