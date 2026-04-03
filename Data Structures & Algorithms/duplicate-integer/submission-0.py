class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for each in nums:
            if each in seen:
                return True
            seen.add(each)
        return False