class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        l = 0
        r = length - 1
        res = 0
        leftMax = 0
        rightMax = 0
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax < rightMax:
                res += leftMax - height[l]
                l += 1
            else:
                res += rightMax - height[r]
                r -= 1
        return res