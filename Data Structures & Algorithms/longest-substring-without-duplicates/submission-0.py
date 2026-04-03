class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        length = len(s)
        left = 0
        right = 0
        res = 0
        for right in range(length):
            # Have we seen this character before, if yes, when? We need to update the starting accordingly
            if s[right] in chars and chars[s[right]] >= left:
                left = chars[s[right]] + 1
            chars[s[right]] = right
            res = max(res, right-left+1)
        return res