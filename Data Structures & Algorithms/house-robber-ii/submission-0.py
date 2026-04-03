class Solution:
    def rob(self, nums: List[int]) -> int:
        def h_rob(arr, l):
            if l <= 2:
                return max(arr)
            first = arr[0]
            second = max(arr[0], arr[1])
            for ind in range(2, l):
                res = max(arr[ind]+first, second)
                first = second
                second = res
            return res
        length = len(nums)
        if length <= 2:
            return max(nums)
        return max(h_rob(nums[:-1], length-1), h_rob(nums[1:], length-1))