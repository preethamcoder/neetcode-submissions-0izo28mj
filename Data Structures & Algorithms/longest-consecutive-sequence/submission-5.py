class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            curr = 0
            if num-1 not in nums:
                curr = 1
                while num + curr in nums:
                    curr += 1
            res = max(res, curr)
        return res