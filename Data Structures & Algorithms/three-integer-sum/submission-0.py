class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        res = []
        for ind in range(length):
            if nums[ind] == nums[ind-1] and ind > 0:
                continue
            ind2 = ind + 1
            ind3 = length - 1
            while ind2 < ind3:
                total = nums[ind] + nums[ind2] + nums[ind3]
                if total < 0:
                    ind2 += 1
                elif total > 0:
                    ind3 -= 1
                else:
                    res.append([nums[ind], nums[ind2], nums[ind3]])
                    ind2 += 1
                    while nums[ind2] == nums[ind2-1] and ind2 < ind3:
                        ind2 += 1
        return res