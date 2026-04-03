class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        curr_max = 0
        for ind in range(length):
            curr_max = max(curr_max, nums[ind]+ind)
            if curr_max >= length-1:
                return True
            elif curr_max == ind:
                return False
        return True
            