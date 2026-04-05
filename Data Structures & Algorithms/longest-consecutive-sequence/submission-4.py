class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return 1
        res = 1
        for each in nums:
            curr = 0
            while each - 1 in nums:
                each += 1
                curr += 1
            res = max(res, curr)
        return res