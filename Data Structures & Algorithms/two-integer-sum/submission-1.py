class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        num_inds = {}
        for each in range(length):
            diff = target-nums[each]
            if diff in num_inds:
                return [num_inds[diff], each]
            else:
                num_inds[nums[each]] = each
