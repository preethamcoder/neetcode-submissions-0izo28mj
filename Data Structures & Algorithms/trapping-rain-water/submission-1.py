class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left = 0
        right = length - 1
        res = 0
        leftMax = 0
        rightMax = 0
        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)
            if leftMax < rightMax:
                res += (leftMax - height[left])
                left += 1
            else:
                res += (rightMax-height[right])
                right -= 1
        return res