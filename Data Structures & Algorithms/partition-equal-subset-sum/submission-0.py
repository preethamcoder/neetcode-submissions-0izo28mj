class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        vals = [False]*(target+1)
        vals[0] = True
        for num in nums:
            for ind in range(target, num-1, -1):
                vals[ind] = vals[ind] or vals[ind - num]
        return vals[target]