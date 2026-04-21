class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        lis = [1]*(length+1)
        for ind in range(length-1, -1, -1):
            for ind2 in range(ind+1, length):
                if nums[ind] < nums[ind2]:
                    lis[ind] = max(lis[ind], 1+lis[ind2])
        return max(lis)