class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqs = {}
        buckets = [[] for _ in range(len(nums)+1)]
        for each in nums:
            if each in freqs:
                freqs[each] += 1
            else:
                freqs[each] = 1
        for each in freqs:
            buckets[freqs[each]].append(each)
        for ind in range(len(buckets)-1, 0, -1):
            for each in buckets[ind]:
                res.append(each)
                if len(res) == k:
                    return res