class Solution:
    def rob(self, nums: List[int]) -> int:
        def h_rob(arr, r1, r):
            l = r-r1
            if l <= 2:
                return max(arr)
            first = arr[r1]
            second = max(arr[r1], arr[r1+1])
            for ind in range(r1+2, r):
                res = max(arr[ind]+first, second)
                first = second
                second = res
            return res
        length = len(nums)
        if length <= 2:
            return max(nums)
        return max(h_rob(nums, 0, length-1), h_rob(nums, 1, length))