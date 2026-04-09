import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        seen = set()
        for s, r, w in times:
            graph[s].append([w, r])
        heap = [(0, k)]
        res = 0
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in seen:
                continue
            res = max(w1, res)
            seen.add(n1)
            for w2, n2 in graph[n1]:
                if n2 in seen:
                    continue
                heapq.heappush(heap, (w2+w1, n2))
        return res if len(seen) == n else -1