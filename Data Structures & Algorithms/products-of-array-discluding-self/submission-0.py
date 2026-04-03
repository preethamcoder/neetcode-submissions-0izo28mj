class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1]*length
        curr = 1
        for each in range(length):
            res[each] *= curr
            curr *= nums[each]
        curr = 1
        for each in range(length-1, -1, -1):
            res[each] *= curr
            curr *= nums[each]
        return res