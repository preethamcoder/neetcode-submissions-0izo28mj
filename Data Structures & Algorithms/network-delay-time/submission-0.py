import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # First, we need to get the grpah and its connections and weights
        graph = defaultdict(list)
        for s, v, w in times:
            graph[s].append((w, v))
        # now, we map what we saw and didnt see
        seen = set()
        heap = [(0, k)]
        res = 0
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in seen:
                continue
            seen.add(n1)
            res = max(res, w1)
            for each in graph[n1]:
                w2, n2 = each
                heapq.heappush(heap, (w1+w2, n2))
        return res if len(seen) ==n else -1