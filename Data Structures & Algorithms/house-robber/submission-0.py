class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return max(nums)
        first = nums[0]
        second = max(nums[0], nums[1])
        for ind in range(2, length):
            res = max(second, nums[ind]+first)
            first = second
            second = res
        return res