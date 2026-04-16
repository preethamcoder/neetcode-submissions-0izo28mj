class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        prefix = 0
        suffix = 0
        length = len(nums)
        for ind in range(length):
            if prefix != 0:
                prefix *= nums[ind]
            else:
                prefix = nums[ind]
            if suffix != 0:
                suffix *= nums[length-ind-1]
            else:
                suffix = nums[length-1-ind]
            res = max(res, max(prefix, suffix))
        return res