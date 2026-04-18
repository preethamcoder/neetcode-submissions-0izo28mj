import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {ind:[] for ind in range(n)}
        for s, d, c in edges:
            graph[s].append([c, d])
        heap = [(0, src)]
        distances = {}
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in distances:
                continue
            distances[n1] = w1
            for w2, n2 in graph[n1]:
                if n2 not in distances:
                    heapq.heappush(heap, (w1+w2, n2))
        for ind in range(n):
            if ind not in distances:
                distances[ind] = -1
        return distances