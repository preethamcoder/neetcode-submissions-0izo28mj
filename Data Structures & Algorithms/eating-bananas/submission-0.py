import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = (l+r)//2
            res = 0
            for p in piles:
                res += math.ceil(p/mid)
            if res <= h:
                r = mid
            else:
                l = mid + 1
        return r