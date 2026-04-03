class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = [0]*26
        w2 = [0]*26
        for each in s:
            w1[ord(each)-97] += 1
        for each in t:
            w2[ord(each)-97] += 1
        return w1 == w2