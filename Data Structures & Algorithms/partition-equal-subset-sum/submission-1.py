class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total //2
        sums = [False]*(target+1)
        sums[0] = True
        for num in nums:
            for ind in range(target, num-1, -1):
                sums[ind] = sums[ind] or sums[ind-num]
        return sums[target]