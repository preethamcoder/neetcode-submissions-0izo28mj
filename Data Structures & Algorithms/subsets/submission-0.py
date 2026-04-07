class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for each in nums:
            res += [[each] + piece for piece in res]
        return res