class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr_sum = 0
        length = len(nums)
        for each in range(length):
            curr_sum += nums[each]
            res = max(res, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return res