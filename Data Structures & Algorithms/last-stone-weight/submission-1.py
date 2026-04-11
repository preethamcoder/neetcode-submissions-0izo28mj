import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1*stone)
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            diff = abs(first-second)
            heapq.heappush(heap, -1*diff)
        elem = heapq.heappop(heap)
        return -1*elem