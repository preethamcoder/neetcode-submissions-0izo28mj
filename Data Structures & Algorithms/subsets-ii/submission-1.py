class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for num in nums:
            res += [[num]+each for each in res if [num]+each not in res]
        return res