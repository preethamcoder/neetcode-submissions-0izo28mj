import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freqs = {}
        for each in nums:
            if each in freqs: 
                freqs[each] += 1
            else:
                freqs[each] = 1
        for each in freqs:
            if len(heap) == k:
                heapq.heappushpop(heap, (freqs[each], each))
            else:
                heapq.heappush(heap, (freqs[each], each))
        return [each[-1] for each in heap]