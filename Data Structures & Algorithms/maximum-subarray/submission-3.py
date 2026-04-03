class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr_sum = 0
        for each in nums:
            curr_sum += each
            res = max(res, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return res