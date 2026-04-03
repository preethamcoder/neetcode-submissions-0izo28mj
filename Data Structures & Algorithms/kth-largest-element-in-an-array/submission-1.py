import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for each in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, (each, each))
            else:
                heapq.heappush(heap, (each, each))
        elem = heapq.heappop(heap)[-1]
        return elem