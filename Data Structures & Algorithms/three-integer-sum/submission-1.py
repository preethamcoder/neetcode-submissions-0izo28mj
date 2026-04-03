class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for ind in range(length):
            if ind > 0 and nums[ind] == nums[ind-1]:
                continue
            ind2 = ind + 1
            ind3 = length - 1
            while ind2 < ind3:
                target = nums[ind] + nums[ind2] + nums[ind3]
                if target < 0:
                    ind2 += 1
                elif target > 0:
                    ind3 -= 1
                else:
                    res.append([nums[ind], nums[ind2], nums[ind3]])
                    ind2 += 1
                    while ind2 < ind3 and nums[ind2] == nums[ind2-1]:
                        ind2 += 1
        return res