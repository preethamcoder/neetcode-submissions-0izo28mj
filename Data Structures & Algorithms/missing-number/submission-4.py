class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        ideal_sum = (length*length + length)//2
        total = 0
        for each in nums:
            total += each
        return ideal_sum - total