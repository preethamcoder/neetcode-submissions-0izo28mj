class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        length = len(s)
        left = 0
        # ind = 0
        res = 0
        for ind in range(length):
            # Have we seen this character before, if yes, when? We need to update the starting accordingly
            if s[ind] in chars and chars[s[ind]] >= left:
                left = chars[s[ind]] + 1
            chars[s[ind]] = ind
            res = max(res, ind-left+1)
        return res