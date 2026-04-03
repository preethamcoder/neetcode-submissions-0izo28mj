import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for each in points:
            dist = -1*(each[0]*each[0]+each[1]*each[1])
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, [each[0], each[1]]))
            else:
                heapq.heappush(heap, (dist, [each[0], each[1]]))
        return [each[-1] for each in heap]